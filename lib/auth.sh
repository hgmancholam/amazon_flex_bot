#alternate method of getting auth token for amazon flex requests

curl -H 
'Host: api.amazon.com' -H 
'Content-Type: application/json' -H 
'Accept-Charset: utf-8' -H 
'x-amzn-identity-auth-domain: api.amazon.com' -H 
'Cookie: session-token="7NB8DBsIelxKhiW4xlLcxdBZmmuetu4Vy4D0NOros5f7l4324VkSFkaxekI2pNw9tZeWGpaJQ3+kI6jQ/JqqPvdttPUwbWiB9A+yyTBAm2fa0XVvm7ouC6XlT8BgCd60qQ5AcKuGixEY5mjqUK1nk3brwOpKHelv8vYebUw44PlAdVKdwcCHMFbWMUv9C7RCgTkud7doBpqhoCmSXbWsqfUSWWkiEp9="; session-id-time=2082787201l' -H 
'Accept: application/json' -H 
'User-Agent: AmazonWebView/Amazon Flex/0.0/iOS/13.6/iPhone' -H 
'Accept-Language: en-US' --data-binary '{"requested_extensions":["device_info","customer_info"],"cookies":{"website_cookies":[{"Value":"\"oFxVhvFtX+bRRX3uNQ3+fQ7qqHjIIHhFJFaZ4qJiQ7hk9a60xRzHvG6eZEKfkgQi2eLthg\/PiN7JaPBJQ8MuR6faoK\/P4N8V2XTmPht+I5MqqZiQG4w0136XamdHt57rd1j5fgGyNHlS9Iv0bha3OsGJPDw97mf3U4f5MvCB\/atJHI4bcAiPaD8G5ZibwAm6EvmU9urTQfOcWZfc56kIhkS0qXcfj8BxtGBW2EdvGx4=\"","Name":"session-token"},{"Value":"2082787201l","Name":"session-id-time"}],"domain":".amazon.com"},"registration_data":{"domain":"Device","app_version":"0.0","device_type":"A3NWHXTQ4EBCZS","os_version":"13.6","device_serial":"02BD3E1B2F1A45F59B6D1BBB4A7DD96E","device_model":"iPhone","app_name":"Amazon Flex","software_version":"1"},"auth_data":{"user_id_password":{"user_id":"shane8061991@gmail.com","password":"SAH.sah.1234"}},"user_context_map":{"frc":"ALUFqY3chE+FrzTY36oUy7br4FtVEOeFHQoYSwtGrOo1DZxSWiRiCAOQZ2u3Z1g69jHGqke3zGxqE9wRSLkA7Bu2wwNkxGMsQVmPg8m2f1nvd6VWvaz64FeTOx0bGeOJ\/QZ0O0\/9GJZYyrxEw\/qH6C9p6Qkv\/RZQJ0YZAj7X+8GMElgMRgxEI5clQFwFOPoiiT0rHg8481eSTrcFmxhKPYyfuo8PTiUKKyndbGEQ+75EIZE6m+BTSSkg1qIwJLvF8\/PXMOTNVo469CxwFnya4jy7lRsxvqjCTML\/NY6dit3E8QC95G54v\/J4n+0pCMo+tv8JvGuRv8NtVnA+iKABGV7m2lXBNaJpIMljvKCkQ\/8vt8+bqiAyPCnxm0wTEZML1jj0fxdifa5EvRJvD4XzZ5atTpCB8QQILQ=="},"requested_token_type":["bearer","mac_dms","website_cookies"]}' --compressed 'https://api.amazon.com/auth/register' | jq '.response.success.tokens.bearer.access_token'
