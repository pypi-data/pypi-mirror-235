import sys
import requests
from fake_headers import Headers
import itertools
from email import policy
from email.parser import BytesParser
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import pandas as pd
from flatten_any_dict_iterable_or_whatsoever import fla_tu
pd_add_apply_ignore_exceptions()
import os
import regex
import bs4
import lxml
import cchardet


def get_fake_header():
    header = Headers(headers=False).generate()
    agent = header["User-Agent"]

    headers = {
        "User-Agent": f"{agent}",
    }

    return headers


def get_html_src(htmlcode, fake_header=True):
    if isinstance(htmlcode, str):
        if os.path.exists(htmlcode):
            if os.path.isfile(htmlcode):
                with open(htmlcode, mode="rb") as f:
                    htmlcode = f.read()
        elif regex.search(r"^.{1,10}://", str(htmlcode)) is not None:
            if not fake_header:
                htmlcode = requests.get(htmlcode).content
            else:
                htmlcode = requests.get(htmlcode, headers=get_fake_header()).content
        else:
            htmlcode = htmlcode.encode("utf-8", "backslashreplace")
    return htmlcode


def parse_html(html):
    r"""
    Parse HTML content and extract information using BeautifulSoup.

    This function takes HTML content as input, parses it using BeautifulSoup, and extracts
    information about the HTML structure, tag attributes, tag text, and the BeautifulSoup
    object for each element found in the HTML.

    Args:
        html (str, bytes, or file path): The HTML content to be parsed. It can be provided as
            a string, bytes, or a file path. If a file path is provided, the function will
            attempt to read the file.

    Returns:
        pandas.DataFrame: A DataFrame containing the extracted information from the HTML.
            The DataFrame columns include 'aa_tag' (HTML tag name), 'aa_attrs' (list of tag
            attributes), 'aa_text' (text content of the tag), 'aa_soup' (BeautifulSoup object
            for the tag), 'aa_old_index' (original index of the tag), 'aa_key' (attribute
            key), and 'aa_value' (attribute value).

    Example:
        from bs42frame import parse_html
        df = parse_html(
            html=r"C:\Users\hansc\Downloads\Your Repositories.mhtml"
        )
        #      aa_tag            aa_text                                          aa_soup  aa_old_index                     aa_key             aa_value
        # 1000   span  Import repository  [\r\n                Import repository\r\n\r\n]           274       ActionListItem-label                class
        # 1001     li                                                                  []           275               presentation                 role
        # 1002     li                                                                  []           275                       true          aria-hidden
        # 1003     li                                                                  []           275                       true  data-view-component
        # 1004     li                                                                  []           275  ActionList-sectionDivider                class
    """
    def instcheck(x):
        return isinstance(x, str)
    multipart_message = get_html_src(html)
    message = BytesParser(policy=policy.default).parsebytes(multipart_message)
    allres = []
    for part in message.walk():
        try:
            content = part.get_payload(decode=True)
            if content:
                s = bs4.BeautifulSoup(content, features="lxml")
                for sx in s.find_all():
                    allres.append([sx.name, list(fla_tu(sx.attrs)), sx.text.strip(), sx])
        except Exception as fe:
            sys.stderr.write(f'{fe}\n')

    df = pd.DataFrame(allres)
    df.columns = ["aa_tag", "aa_attrs", "aa_text", "aa_soup"]
    df["aa_old_index"] = df.index.__array__().copy()
    df = df.explode("aa_attrs").reset_index(drop=True)
    df2 = df.aa_attrs.ds_apply_ignore(
        [pd.NA, pd.NA],
        lambda q: [
            q[0],
            list(itertools.takewhile(instcheck, q[1]))[0],
        ],
    )
    df2 = df2.to_frame().apply(
        lambda x: x[df2.name if df2.name else 0], result_type="expand", axis=1
    )
    return (
        pd.concat([df, df2], axis=1)
        .rename(columns={0: "aa_key", 1: "aa_value"})
        .drop(columns="aa_attrs")
    ).drop_duplicates(subset=['aa_tag', 'aa_text','aa_old_index', 'aa_key', 'aa_value']).reset_index(drop=True)

