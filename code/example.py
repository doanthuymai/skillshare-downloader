from downloader import Downloader

cookie = """
device_session_id=31a5e8da-2c11-4aa0-ab86-5df4ab58b503; show-like-copy=1; YII_CSRF_TOKEN=djNRaWJxMUVDTEMyRjhsbmRQY0hsVFhFc1NjQWRDSTdjLdcFzJnMH8aNWDW_xOGSRcRjSeLErFUV584fJHaZbg%3D%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; _gcl_au=1.1.2133738230.1600786674; _pin_unauth=dWlkPU5EVmlZbVJrWVRFdE1UQTFNUzAwTVdRMUxUa3dPR1F0TUdRM01HSXpNV1l5T0RVMiZycD1abUZzYzJV; sm_uuid=1600787674163; __stripe_mid=234756d2-3626-4342-b3d8-22d5d1618598591329; __stripe_sid=67a13367-bb59-481e-8f63-f8bb4fb7ca3c8bc7d1; __pdst=53e930f9295147f0ae330602701f287d; IR_gbd=skillshare.com; _scid=42008d82-bdcd-4290-bee8-94699c125130; CAPTIONS=off; _sctr=1|1600707600000; __ssid=5c0596e3d537ecf079a1a9b97dcb01b; G_ENABLED_IDPS=google; PHPSESSID=97da28b665ce2d8805e3a5d65b1d2763; skillshare_user_=adf1ab850dfdf5050327e0407e1e983da3f49989a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2215705933%22%3Bi%3A1%3Bs%3A18%3A%22fln81349%40eoopy.com%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A2%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22514292388%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222020-09-22%2015%3A22%3A36%22%3B%7D%7D; loc=%7B%22lat%22%3A%2221.022%22%2C%22lng%22%3A%22105.84%22%2C%22cid%22%3A%220%22%2C%22city_name%22%3A%22Hanoi%22%2C%22city_district%22%3A%22%22%2C%22region%22%3Anull%2C%22region_code%22%3Anull%2C%22country_code%22%3A%22VN%22%2C%22country%22%3A%22Vietnam%22%7D; ss-ref=%7B%22teacher%22%3A%7B%226595003%22%3A%7B%22classId%22%3Anull%2C%22referralType%22%3A%22affiliate%22%7D%7D%7D; visitor_tracking=utm_campaign%3D318573%26utm_source%3DIR%26utm_medium%3Daffiliate-referral%26referrer%3Dhttps%3A%2F%2Fvuihocweb.com%2F%26referring_username%3D; IR_4650=1600790440740%7C-1%7C1600786676457%7CxsRWvlSbMxyOU7vwUx0Mo3QUUkiS0oVQXWRDUw0%7C; IR_PI=731da9b5-fce7-11ea-bc5c-0abbe301118c%7C1600876840740; ss-subscription-coupon=referral2m
"""

dl = Downloader(cookie=cookie)

# download by class URL:
# dl.download_course_by_url('https://www.skillshare.com/classes/How-to-Develop-12-Vuforia-Augmented-Reality-Apps-in-2-hours/1664713776?via=search-layout-grid')

# or by class ID:
dl.download_course_by_class_id(1664713776)
