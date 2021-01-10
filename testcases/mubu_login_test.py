# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\mubu_login.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuLogin(HttpRunner):

    config = Config("login").verify(False)

    teststeps = [
        Step(
            RunRequest("/login")
            .get("https://mubu.com/login")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1610268759",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1610244987",
                    "SESSION": "f4257d1a-bb99-4b96-9680-e5c6642eaf70",
                    "SLARDAR_WEB_ID": "627a324d-1525-4012-a443-4dd5a38741f6",
                    "_ga": "GA1.2.1478645020.1610244987",
                    "_gat": "1",
                    "_gat_UA-77727571-3": "1",
                    "_gid": "GA1.2.2087299800.1610244987",
                    "country": "US",
                    "csrf_token": "3f8a84d5-05b1-4568-b776-332e1c64ce18",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "data_unique_id": "14a656ae-aec4-4715-8e5b-cead72d29520",
                    "language": "en-US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "987897cf-710c-4420-8f19-176eb7f41d3",
                    "reg_from": "https%3A%2F%2Fwww.google.com.hk%2F",
                    "reg_prepareId": "176eb7f3d8a-176eb7f3d7a-4420-8f19-27d891871473",
                    "use-redesign": "1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
            .get("https://mubu.com/login/password")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "referer": "https://mubu.com/login",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1610268763",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1610244987",
                    "SESSION": "f4257d1a-bb99-4b96-9680-e5c6642eaf70",
                    "SLARDAR_WEB_ID": "2cca9f4b-9ef6-4ee5-a0aa-0a2f29d876ae",
                    "_ga": "GA1.2.1478645020.1610244987",
                    "_gat": "1",
                    "_gat_UA-77727571-3": "1",
                    "_gid": "GA1.2.2087299800.1610244987",
                    "country": "US",
                    "csrf_token": "3f8a84d5-05b1-4568-b776-332e1c64ce18",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "data_unique_id": "14a656ae-aec4-4715-8e5b-cead72d29520",
                    "language": "en-US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "7ce9b7ae-6352-4acb-af0f-176eb7f6403",
                    "reg_from": "https%3A%2F%2Fwww.google.com.hk%2F",
                    "reg_prepareId": "176eb7f62f6-176eb7f625b-4acb-af0f-976a9096745c",
                    "use-redesign": "1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
            .post("https://mubu.com/api/login/submit")
            .with_headers(
                **{
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "47",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/login/password",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1610268765",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1610244987",
                    "SESSION": "f4257d1a-bb99-4b96-9680-e5c6642eaf70",
                    "SLARDAR_WEB_ID": "c21176ef-c55b-4160-9a14-f6078e77132e",
                    "_ga": "GA1.2.1478645020.1610244987",
                    "_gat": "1",
                    "_gid": "GA1.2.2087299800.1610244987",
                    "country": "US",
                    "csrf_token": "3f8a84d5-05b1-4568-b776-332e1c64ce18",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "data_unique_id": "14a656ae-aec4-4715-8e5b-cead72d29520",
                    "language": "en-US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "7ce9b7ae-6352-4acb-af0f-176eb7f6403",
                    "reg_from": "https%3A%2F%2Fwww.google.com.hk%2F",
                    "reg_prepareId": "176eb7f62f6-176eb7f625b-4acb-af0f-976a9096745c",
                    "use-redesign": "1",
                }
            )
            .with_data(
                {"password": "1220jj", "phone": "17625416583", "remember": "true"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/app")
            .get("https://mubu.com/app")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "referer": "https://mubu.com/login/password",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1610268765",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1610244987",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "SESSION": "f4257d1a-bb99-4b96-9680-e5c6642eaf70",
                    "SLARDAR_WEB_ID": "c21176ef-c55b-4160-9a14-f6078e77132e",
                    "_ga": "GA1.2.1478645020.1610244987",
                    "_gat": "1",
                    "_gid": "GA1.2.2087299800.1610244987",
                    "country": "US",
                    "csrf_token": "3f8a84d5-05b1-4568-b776-332e1c64ce18",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "data_unique_id": "14a656ae-aec4-4715-8e5b-cead72d29520",
                    "language": "en-US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "7ce9b7ae-6352-4acb-af0f-176eb7f6403",
                    "reg_from": "https%3A%2F%2Fwww.google.com.hk%2F",
                    "reg_prepareId": "176eb7f62f6-176eb7f625b-4acb-af0f-976a9096745c",
                    "use-redesign": "1",
                    "user_persistence": "fb76fe60-4f34-463b-8e58-76ad1c09d90f",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/")
            .get("https://api2.mubu.com/v3/")
            .with_headers(
                **{
                    "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "image",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1610268765",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1610244987",
                    "SLARDAR_WEB_ID": "c21176ef-c55b-4160-9a14-f6078e77132e",
                    "_ga": "GA1.2.1478645020.1610244987",
                    "_gat": "1",
                    "_gat_UA-77727571-3": "1",
                    "_gid": "GA1.2.2087299800.1610244987",
                    "use-redesign": "1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 17)
            .assert_equal("body.msg", "illegal request")
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .post("https://api2.mubu.com/v3/api/message/get_message_unread")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "7b2b0c37-d557-4a97-9a5d-349cf9aafd2e",
                }
            )
            .with_json({"page": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
            .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "12",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "d7ddc04c-46af-4e8a-9950-76944ea5da90",
                }
            )
            .with_json({"start": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "0",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "dd6de712-4220-457f-87b8-36019e3cc360",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
            .get("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "afe5d7fe-5779-42db-a9da-2e7bf35f5530",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "30",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "37ca5869-a410-4fa9-89a4-e0fbdd084545",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
            .post("https://api2.mubu.com/v3/api/user/get_user_params")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "0",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "34d411c5-32bc-419e-b432-b5a49afb1e86",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .post("https://api2.mubu.com/v3/api/advertisement/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "ab234a98-f611-4f9c-a66a-c8c39b700622",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "30",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "0ab1e930-5321-11eb-a1bd-ad0c581d182d",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTU2NDkxMyIsImV4cCI6MTYxMjg2MDc3MCwiaWF0IjoxNjEwMjY4NzcwfQ.69kT7kwvkk5WkDDBYVFw81c1tnFpA7UCy6WPji5McJPuT0hfK1L-uwkMIcYMzUTUWfBc534pntZSntsoVx5pBg",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "version": "3.0.0",
                    "x-request-id": "37ca5869-a410-4fa9-89a4-e0fbdd084545",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuLogin().test_start()
