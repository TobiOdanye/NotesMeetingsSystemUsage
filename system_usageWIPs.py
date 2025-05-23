import requests
import time
import pandas as pd
import re
from datetime import datetime, timedelta
import re
import os
import numpy as np
from itertools import cycle
import streamlit as st

def fetch_api_tokens():
    api_tokens = [
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOTNkOWE1NTRiNTBkMDJkZDlkYTQzMDIzYWU5OTM2ZGRkZ"
    "GEyNmU1YjRkMDYxMzFhNGFiYzc2NDNkMjY4YTYxN2ZlZjY4NjJlZWVmZjVjMTgiLCJpYXQiOjE3MzY0MzA4NjYuODkzNjM0LCJuYmYiOjE"
    "3MzY0MzA4NjYuODkzNjM5LCJleHAiOjQ4OTIxMDQ0NjYuODg4ODAzLCJzdWIiOiIxOTc0ODU3Iiwic2NvcGVzIjpbXX0.DtP-949ngXZ4N"
    "PEW9aAaPxK9pcb7WOuru35ZzDCFWv-i2OwefloSIPIn6Q75Gd7EM5-1PNp55kpl5IENS_CXI3Xo0x4P_a9YHwXerWhbylEcVauB_oE5JIV"
    "laA5d9yQhbrv7Xf2wzBMP7By0ANcpqobAl7ld_DgVF-YA5zzhvhh2itAbtnXOv8jG_K56BhfECwC9HK2J2vihVJmgxWp_n9jjZShOMnlTz"
    "Rf4OIf0bUPLtZV3tI1VlyTLoR0kBH4Osu6uYHw5QkMqAil23uuDqopHaAI-6w1U9tWuZV7PkS_tdkbjpGYgeKLdm6gpenFyVLcUzyAySoE"
    "Z2NH5eKCLg_TPOw7BxJGjY_K15UpBl0EIe59zZjtwZA_CW1QfhRAS27MwA-7TDkPNeQWNKFn8TdlsySidHI7J7lfmG0KB4793pUMjljvA3"
    "_wvh1ZKnplFQ10y_fXcmCyuQrKM44Vl6ZaLD78wQ-q_fN88tSaV4Avq1Z80XzsTfJEkfoG2Lnpa61760CyXG0v3l6R0i_U4SQk1FdwhuPp"
    "_cP3hLyu9BrFLRt4u53lMmTa_5J72rRzbGBVeZjjJBOXFy3Y9J-OM7H4u4Kz0QIZhyN3XB2lXgHy7VZcsRuQhb6X39W3Ukk0ZyuCZeEWK4"
    "mn_Uf7i9d4uiDuLalRhu-vHXpOHsyAvQl0",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiMjM5Y2Q1N2I0MGI1MjBhN2Y5NGRhMzE0ZjdlMDIwMm"
    "JkMmViNDFjNjU5YTkxNjRhOTRjYWEwZjRkOTYzOTFiMjkxNzY5NzNiNzAwYTJlODIiLCJpYXQiOjE3MzM4NDczNDguOTkyNzQyLCJuY"
    "mYiOjE3MzM4NDczNDguOTkyNzQ1LCJleHAiOjE3NjUzODMzNDguOTc1NTAyLCJzdWIiOiIxOTczNjY2Iiwic2NvcGVzIjpbXX0.jgIg"
    "ZkAsB-Ncivv5lyJCQx3XvABRbIpUThmLtb7AENe0S8e3lwKSBkyE_QbrFqIYa-z4p0J42OkQz0uv-h_aepG_7OhdlKzpe3eSECZY1LE"
    "RRtqdTIsO9gBx0Wqxul7ixOaAJHdjpHCHS_eXaZKLu3_OhTEkyAD8EHILlbv6Uc3R2cOtpY5s3rJEFffcPIN7tmuZ7Mmeo9SJXpnSdb"
    "4qg6REJsO5YLFPUpvZyZn1G9SwVfpZAP0nfbrTuXKIwo6gbX22R_UZGL_n2rHnObUqKyRUdS8XCEuZfQNge6_VwT2vsb72rNMK4Dw5S"
    "m4jeQEcdbRMaB-rr0YpkFXyMAhHsV8cimfmDPro_NxUV2dXONtlfZhGFySPbAckncCZq7geMLXhP-MYOm3FxPsiI7FFw3_LsQyNICs4"
    "Hndy8ccKe_sPldWWV6eq7E2OYQcpOfrcRjk4YrnVl1fJL_krxVYvf_JwYqRb9GCpjpdBScWlKWc549HnqKtx-jD8S_QOjgDCuVgXwbg"
    "wggmcKLCb9AEAL3zcKwOSoxQ4Bqg8XMqHLiSoUs-KwHxj6bpi1xXzeaCTN84sV1jK4TO99v_bjHGkBSP9H6sbwEViPdaD9MmjMOv0C5"
    "z-PdGTf7cRQm6kee0F7Q6gk7J-nRBGV5unL0il7S9gd2UXZc7xsJV3hkm8Qws",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNWY1NGY5NzBmMWJlNDEyNDUwZGI2ZjczMWRjNzA2NTI"
    "4NmVkMzRhMGQxMGVkODZmYzY0OWI1NWFlN2E1MWE1M2Q4M2Q2N2FhMjAwNTk2ZGIiLCJpYXQiOjE3MzY3OTAzMzQuOTYzNjE3LCJuYmYi"
    "OjE3MzY3OTAzMzQuOTYzNjIsImV4cCI6NDg5MjQ2MzkzNC45NTc0NTMsInN1YiI6IjE5NzUwNzUiLCJzY29wZXMiOltdfQ.f-nZneDlXj"
    "G8cAk8VJuvJYBw9jBToBx3cL-I2uFqTjvhoX4oqoYsAQPvTIMhOJLXwL8yYxl1bPWro7ynjx-HiZu0w5PylnZzDPWxZQlBCYluLIOIoel"
    "4_mdpZvF0Jb-755dWLkWsT9Yxn86PjwtDqDizZzXGML8r3TIwlFwD03wSMvOKdZK7Uc7x8u2NZBq4jIS7eZM0sQtM5dciyPEk8S03Z5TG"
    "MUxye2zWAp9iAXXRStdPGs1pwe3UTWIjbyMBTLMmUDuKYzixXOVmzkkyL5IiqGfrbm4fHfk4s-C4B8jnFnUpkaGtGGAaT8mdKJmjNeFla"
    "1xg3XG306TSJ7dfYDV9NyGav0okQbERSPL5wRG9m9CrgMdzad7U08MuV8glST3koHY0TZguNtL-G4m7luPfQIK26EXmrCJI2jL7keBgcU"
    "N9Pck0hmUQiCbyn01L-rC8pU6i-R4a9mqKYVtlOfDHTcSuUyPtoa1EE-WA-rSY4cLtTtRqwJUCv3_1rQ2lhMfe0TfL-DRDvwfhyxF8xy0"
    "kygYPfs83wL4UkxTZxZnsAUjv51G-302ZLqrBVLkODOSLmAWJgLBu1BsvW7bKXUwQCLcut2RfPn9OhnS75Tu3qUvAq7uXNwNPH6zw0j53"
    "9rOlHt3A4TgkFiOZzjKvBhr1WT7ZuzHWUYPvLjdv1fw",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNTAwZmIyNDU4OWVmYmI4MWRiNmVmMmJhZmI3ODA1ZjEy"
    "ZTIyN2RjM2NhMjYzNmYzYzI1NGY3ODI5ZDlmMmFiYzEwMjllN2EwMTUyNjBiNGYiLCJpYXQiOjE3MzY4NTEzODUuNDg0MDU3LCJuYmYiO"
    "jE3MzY4NTEzODUuNDg0MDYsImV4cCI6NDg5MjUyNDk4NS40Nzk5NDUsInN1YiI6IjE5NzUxMTAiLCJzY29wZXMiOltdfQ.iXjyYV6C7zj"
    "Z6-f6KZ3EFrdS_R1ntjv4X-LgV4wZqz5wHRVM1AbotaDJi2dtuFVludJWBhXlLEu32FpsB1Ogrk0pBe2ELB3HcN6Rc80uUBHUDo8Xbtux"
    "e_dhtOcP9ZsDEltDsvSBznzGWUSqaxHu3BxpBfhlmLwzjhbA2SLkKbMo_LnlnuenpKSAxnpwExuuvY4znPLZhSBHdfdPABdkchPfCX7Js"
    "Lp58ZvMqyZ8zjJ1fRcjfpBz6VybxIW9oErtGRsXfdU5eUX6hW2MWgtNkW6iU09k_Ge4C7ag4QaQTWkLkM2DjLOoLByXm3b1URv04suYDK"
    "FGAUmO9zapAqjYJ2ljp8yrqpRnLnmr7ltQHQ-nZezUQZJDdvIM5kWANLMQEax9xPAB6EbTouXFf8X8NjiCtbAAJcPPLAHsxPX5CW9DVMW"
    "-tw1zsHC06Jg_ou3LMd-XUPilF86iXC_1pP_0dbgCDa7GZEaV_ptiQ24LqD1QSkKt7qXVvxmoO2Ktu4mJez1tzs6prThke9YiijG9FJND"
    "a4Tnj6K_DCsx_IJwaoCBFQjM7l_EaIAYTgh49nPojPGfXop-_oIxcEhJN1ZH26syhC2rARV84vQ30h1VerRWWddWP8mxjx0lIv3oRiG6v"
    "gvyR-iD9nyVW41NOykKGDv9GaAexB4PkgRJ7pjUkFw",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYjFjZGU4ZmNiOGM2MjQxZWVkN2E3ZDk3NDhmMWJlMzgyY"
    "Tc2MmY2ZjBkZjI0NmY4MGFmZjJkMjA0NmJmYjZiZTAwM2ExNzY5YTVlYzYzMDciLCJpYXQiOjE3MzY5NTQzMDUuNjA3NzIyLCJuYmYiOjE3"
    "MzY5NTQzMDUuNjA3NzI1LCJleHAiOjQ4OTI2Mjc5MDUuNjA0MDEyLCJzdWIiOiIxOTc1MjI1Iiwic2NvcGVzIjpbXX0.oFYuSb5P0ESf7cH"
    "tHVGqR-2FMwUKycawpb_gUKAqzOzPf_-y5yri8AyK8-ssKZ7-hZn4utzMTxHmeJ8rFWCpW1rrJhI1EfrcjqDS_z4P_smbDEeIwABVLBvm4t"
    "fZCQAGwHSvt7SEIfjP_YNU5R2sF_natkqqAvqCdzmcmJoLJP6-kCO5vlOwsTKtYQhus7IKeyHbyXBqdAm5MXi85uLeeZvYlu-BIcwiN6xwe"
    "aLSyBlR44gqiliDsAbb0GmQ9IFQq2Mjmt7m3ajsVdF_HeQJVZyvSKTn_QEZ9rp40x7CwaYxsECcmBfUTWbTs5fdj3ZUznvnn6yFOFzTt0IY"
    "yvRo-v0ZDiIOMqNVJ5jzQXlBUb39YHljKVLZBQguC4UijWIOTkpGpbhLNaueO3FjwBPji0jqCIblxmyRC3QhzTEJOJcduAV8HSh7sILkWoA"
    "x05j2ShRPhu9ri2uIGZzEL2_H27CKqWIap66MCWz0npfPgH1L1LHiOKxIK9oV1X7fUJM9ol1KAHmacrT88y-JotHgKqcd1GseVWLQzlm3-o"
    "Q0-LIiwbSZOfIHSF3a8u5MGhtGrtVTEQnxubQ-rfo6IKTCWHAj_zc3DdySdsmakejZ7_JkLDP414JkGgFEiMhB9tz3weOsCavHPm80cjr2P"
    "bAb6NTWFlMTy-AyMSsq60b85jA",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiNjQ4MjQzMWI3ZWMwZGMwYTVmMWYxY2Q2ZDdjMThiZjkyOW"
    "FmYjljNDhjNmY2MDI2YTdkMWVjZjMyNWJiY2Q0MjY3MGU2ZjFmNjdkNjIxMTAiLCJpYXQiOjE3MzY5NTQzNzMuMjI1MDAzLCJuYmYiOjE3M"
    "zY5NTQzNzMuMjI1MDA3LCJleHAiOjQ4OTI2Mjc5NzMuMjIwNDM0LCJzdWIiOiIxOTc1MjI2Iiwic2NvcGVzIjpbXX0.EEs7cwr17uZ7E-Mj"
    "jYNehnhkcuWEhVF-HIQEU78pLpv0_8MxgIF0KufjHwb60hhdlh2kuNh2DKssq8F7E3aHvPXYOtrnYQvq4GBLM0Q2LeRG3dKduCdC6iBC0h4"
    "EJX3DlJ-yWfRbjmcURjAC0wPCU0_5rv89eLLZJRWAYTJIS1X1MXhvkt1fu0DsQl3PdbZ-EaWRdp88CgK9RTDtwx4V-mNLp_WrhZ541D_fbw8"
    "ZVcISMPMRRhhetDxB3mBrLkWt23A44uPS4Kq4vHPNwBxzLhIgBtdcm-PAqitFnfC4p5b9V_ntWXLTkcEY2X7LoI1xwYh8OIZaXjiLdBqJOP"
    "tifdLXaeW_diGgr6SoUngNN2WE-tY0U9PKx_Xua8-kSitMZFnwKPOmKA2CqOgLy97sG_eA1LF8bY3krYqVS8B9vnfT1_KEotcQO5LYiTM6fR"
    "vWK9Ki9CLBVmot6Bv7XYOWoF7DQgFx7jEGmWGV3HR1P1SOgDZ9ZZaOxPm8RIDUPmVrc2CocWkWTbYa0wE5KwrnzZT5GDBxJp5QCQyjQ_7rhv"
    "jMeO8FQxOqJTvIE5iKmoBDUqUr4G58XNYVdBxi9xcnsQSCHU8VRUlGdFYP0r71sFMmzQCqOY7hu84odb1aS3_vko7yynm54wfGO8auG7pgqS"
    "fRM5_84z9y4BaLzbRDyFQ"]
    return api_tokens


def fetch_meetings(api_tokens):
    print('testing3')
    api_token = api_tokens[0]

    # Ezekia URL for total meeting and page (api) count
    base_url_agg = "https://ezekia.com/api/meetings?page=1000000"

    # Headers to authenticate API request for total counts
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"  # Adjust content type if necessary
    }

    # API request (GET request) for total counts
    response = requests.get(base_url_agg, headers=headers)

    # Extract the "total" and "last_page" values
    total_meetings = response.json()['meta']['total']
    last_page_meetings = response.json()['meta']['last_page']

    # Print the extracted values
    print(f"Total Meetings: {total_meetings}")
    print(f"Total Pages: {last_page_meetings}")

    # Loop through pages in Ezekia API and store in dataframe
    meetings_list = []
    for page in range(1, last_page_meetings + 1):

        api_token = api_tokens[(page - 1) // 3 % len(api_tokens)]

        # Headers to authenticate API request for total counts
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"  # Adjust content type if necessary
        }

        page_url = f"https://ezekia.com/api/meetings?page={page}&order=desc"
        page_response = requests.get(page_url, headers=headers)

        if page_response.status_code == 200:
            page_data = page_response.json()  # Get the JSON response for the current page

        for meeting in page_response.json()["data"]:
            meeting_date = pd.to_datetime(meeting["date"][:10])
            meeting_organizer = meeting["organizer"].split(" <")[0].strip().split(" | Encore Search")[0].strip()
            meeting_title = meeting["title"]
            print(meeting_title)

            # Step 1: Set January 1st of the year as the start of Week 1
            start_of_year = pd.to_datetime(f'{meeting_date.year}-01-01')
            days_to_sunday = (6 - start_of_year.weekday()) % 7
            first_sunday = start_of_year + pd.Timedelta(days=days_to_sunday)
            days_since_first_sunday = (meeting_date - first_sunday).days
            if days_since_first_sunday < 0:
                meeting_week = 1  # The date is within Week 1
            else:
                meeting_week = (days_since_first_sunday // 7) + 2

            meeting_month = meeting["date"][5:7]
            meeting_quarter = meeting_date.quarter
            meeting_year = meeting["date"][:4]

            if meeting["tag"] is not None:
                meeting_tag = meeting["tag"]["text"]
            else:
                meeting_tag = None

            meeting_company = ', '.join([entry['name'] for entry in meeting["channels"] if
                                         meeting["channels"] and entry['type'] == 'client' and entry[
                                             'label'] == 'company']) or None

            meeting_consultants = ', '.join([entry['fullname'] for entry in meeting["assignees"] if
                                             meeting["assignees"] and entry['type'] == 'candidate']) or None

            if meeting["channels"]:
                context_name = ', '.join(entry["name"] for entry in meeting["channels"] if
                                         entry["type"] in ["opportunity", "list", "assignment", "person"]) or None
            else:
                context_name = None

            if meeting["channels"]:
                context_label = ', '.join(entry["label"] for entry in meeting["channels"] if
                                          entry["type"] in ["opportunity", "list", "assignment", "person"]) or None
            else:
                context_label = None

            # Append extracted values to the list
            meetings_list.append({"Date": meeting_date, "Year": meeting_year, "Week": meeting_week, "Type": 'Meeting',
                                  "Author": meeting_organizer.split()[0], "Note Name(s)": None, "Note Type(s)": None,
                                  "Note Header": meeting_title, "Note or Meeting Tag(s)": meeting_tag, "Company": meeting_company,
                                  "Consultants": meeting_consultants, "Context Name(s)": context_name,
                                  "Context Type(s)": context_label})

    # Create a DataFrame from the list of meeting data points
    meetings_df = pd.DataFrame(meetings_list).reset_index(drop=True)
    meetings_df = meetings_df[meetings_df["Year"] == '2025']
    meetings_df = meetings_df[["Author", "Week", "Date", "Type", "Note Type(s)", "Note Header", "Note Name(s)", "Note or Meeting Tag(s)",
                               "Context Type(s)", "Context Name(s)"]].sort_values(by="Date", ascending=False)
    
    return meetings_df


def fetch_notes(api_tokens):
    base_url_agg = "https://ezekia.com/api/notes?noteType=user"

    headers = {
        "Authorization": f"Bearer {api_tokens[0]}",
        "Content-Type": "application/json"
    }

    response = requests.get(base_url_agg, headers=headers)
    last_page_notes = response.json()['meta']['lastPage']
    print(f"Total Pages: {last_page_notes}")

    user_notes_list = []
    for page in range(1, last_page_notes + 1):
        api_token = api_tokens[(page - 1) // 3 % len(api_tokens)]
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        page_url = f"https://ezekia.com/api/notes?noteType=user&sortBy=%60createdAt%60&sortOrder=desc&page={page}"
        page_response = requests.get(page_url, headers=headers)

        if page_response.status_code == 200:
            print(f"Fetched notes page {page} from Ezekia API")
        else:
            print(f"Failed to fetch data for page {page}. Status Code: {page_response.status_code}")

        for note in page_response.json()["data"]:
            note_date = pd.to_datetime(note["date"][:10])
            note_author = note["author"]
            note_type = ', '.join([i["text"] for i in note["tags"]]) if "tags" in note and note["tags"] else None
            note_notable_id = note["notable"]["id"] if "notable" in note and note["notable"] else None
            note_notable_type = note["notable"]["type"] if "notable" in note and note["notable"] else None
            note_notable_name = note["notable"]["name"] if "notable" in note and note["notable"] else None
            note_context_project_id = ', '.join([str(i["projectId"]) for i in note["context"]]) if "context" in note and \
                                                                                                   note[
                                                                                                       "context"] else None
            if note_context_project_id is not None:
                note_context_project_id = note_context_project_id.replace(', None', '').replace('None, ', '').replace(
                    'None', '').strip()
            note_context_type = ', '.join([i["type"] for i in note["context"]]) if "context" in note and note[
                "context"] else None
            note_context_name = ', '.join([i["name"] for i in note["context"]]) if "context" in note and note[
                "context"] else None
            note_text_header = note["textStripped"].split('\n')[0]

            start_of_year = pd.to_datetime(f'{note_date.year}-01-01')
            days_to_sunday = (6 - start_of_year.weekday()) % 7
            first_sunday = start_of_year + pd.Timedelta(days=days_to_sunday)
            days_since_first_sunday = (note_date - first_sunday).days
            if days_since_first_sunday < 0:
                note_week = 1
            else:
                note_week = (days_since_first_sunday // 7) + 2

            note_month = int(note["date"][5:7])
            note_quarter = note_date.quarter
            note_year = int(note["date"][:4])

            user_notes_list.append(
                {"Date": note_date, "Year": note_year, "Week": note_week, "Month": note_month, "Quarter": note_quarter,
                 "Author": note_author.split()[0], "Note or Meeting Tag(s)": note_type, "Notable ID": note_notable_id,
                 "Type": 'Note',
                 "Note Type(s)": note_notable_type, "Note Name(s)": note_notable_name,
                 "Context Type(s)": note_context_type, "Context Name(s)": note_context_name,
                 "Note Header": note_text_header})

    user_note_df = pd.DataFrame(user_notes_list)
    user_note_df = user_note_df[["Author", "Date", "Week", "Type", "Note Type(s)", "Note or Meeting Tag(s)", "Note Name(s)",
                                 "Context Type(s)", "Context Name(s)", "Note Header"]][
        user_note_df["Year"] == 2025].sort_values(by="Date", ascending=False)

    return user_note_df


# ---------- Streamlit App ----------
st.set_page_config(page_title="Notes and Meetings System Usage (2025)", layout="wide")
st.title("Mandate System Usage - WIPs (2025)")

@st.cache_data(show_spinner="Loading notes from Ezekia API...")
def load_notes_meetings():
    api_tokens = fetch_api_tokens()
    notes = fetch_notes(api_tokens)
    meetings = fetch_meetings(api_tokens)
    combined_df = pd.concat([notes, meetings], ignore_index=True)
    combined_df = combined_df[["Author", "Week", "Date", "Type", "Note Type(s)", "Note Header", "Note Name(s)", "Note or Meeting Tag(s)", "Context Type(s)", "Context Name(s)"]]
    combined_df = combined_df.rename(columns={col: col.replace('note', 'note or meeting') for col in combined_df.columns if 'note' in col})
    
    return combined_df

# Load and cache notes once
notes_meetings = load_notes_meetings()

# ---------- Filters ----------
author_input = st.text_input("Filter by Author")
week_input = st.number_input("Filter by Week", min_value=1, max_value=53, step=1, format="%d")
type_input = st.text_input("Filter by Meeting or Note")
context_project_input = st.text_input("Filter by Mandate Name (partial match allowed)")

filtered_notes_meetings = notes_meetings.copy()

if author_input:
    filtered_notes_meetings = filtered_notes_meetings[filtered_notes_meetings["Author"].str.lower() == author_input.lower()]

if week_input:
    filtered_notes_meetings = filtered_notes_meetings[filtered_notes_meetings["Week"] == week_input]

if type_input:
    filtered_notes_meetings = filtered_notes_meetings[filtered_notes_meetings["Note or Meeting Tag(s)"] == type_input]

if context_project_input:
    filtered_notes_meetings = filtered_notes_meetings[filtered_notes_meetings["Context Name(s)"].str.contains(context_project_input, case=False, na=False)]

# ---------- Display ----------
st.write(f"### Showing {len(filtered_notes_meetings)} notes")
st.data_editor(filtered_notes_meetings.reset_index(drop=True), use_container_width=True, disabled=True)

