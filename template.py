# Author: Rajesh Kumar
# Date:   2020-10-16 
# Scrape:  New Url


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import functions as fn
from functions import ET
from datetime import date,datetime, timedelta
import time
from socket import error as SocketError
import re
from time import sleep
from googletrans import Translator
# Don't remove
# import ml.cpv_classifier as classifier
# from false_cpv import false_cpv


# import ml.cpv_classifier as classifier
# import ml.africa_classifier as classifier
# import ml.cis_classifier as classifier
# import ml.middle_east_classifier as classifier

# try:
# 	from googletrans import Translator
# 	translator = Translator()
# except:
# 	pass
# title_en= translator.translate(title, dest='en').text


# def translatorlanguage(sent_orginal_langauge, dest_lang):
#     translator = Translator()
#     trn = translator.translate(sent_orginal_langauge, dest=dest_lang)
#     return (trn.text)
# title_en = translatorlanguage(sent_orginal_langauge=title_en_org, dest_lang='en')

NOTICES = ET.Element("NOTICES")

ml_cpv = 0
notice_count = 0

try:

	'''
	with open('assets/cpv_dict.csv', 'r') as f:
		reader = csv.reader(f)
		maps = list(reader)
	cpv_dict = dict(maps)
	'''

	PROXY = "103.58.249.164:23500"   # india proxy ip:port
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

	# chrome_options = Options()
	# chrome_options.add_argument("--headless")


	# Don't remove
	# days = fn.last_success('internal_code') - 1
	th = date.today() #- timedelta(days)
	threshold = th.strftime('%Y/%m/%d')
	print("Scraping from or greater than: " + threshold)

	flag = 1

	try:
		driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe')
		# driver = webdriver.Chrome(chrome_options=chrome_options)
		page = webdriver.Chrome(chrome_options=chrome_options)
	except SocketError as e:
		time.sleep(10)
		driver = webdriver.Chrome(chrome_options=chrome_options)
		page= webdriver.Chrome(chrome_options=chrome_options)
	# driver.set_window_size(1920, 1080)
    # page.set_window_size(1920,1080)

	url = ''
	driver.get(url)

    ############# pagination for each page
    for i in range(10):
        if (i>0):
            print('-------------------' 'Page Number: ' +str(i)+ '-----------------------------')
            driver.find_element_by_id('').click()
            sleep(4)
        ########### end pagination 

		tenders = driver.find_elements_by_css_selector('')
		tenders_len = len(tenders)
		# Check tender len is greater then 
		if tenders_len<0:
			break    # terminated 

		for tender in tenders:


			#code
			# add resource url 
            
            # resources = []
            # pdfclick = driver.find_elements_by_class_name('fa-file-pdf')

            # for i in range(len(pdfclick)):
            #     driver.find_element_by_class_name('fa-file-pdf').click()
            #     time.sleep(4)
            #     directory = 'html/temp_files/' + folder + '/' + internal_code
            #     filePath = max([directory + "/" + f for f in os.listdir(directory)], key=os.path.getctime)
            #     reseouceUrl = 'http://ftp.dgmarket.com/scraped/' + filePath
            #     reseouceUrl = reseouceUrl.replace('/html/temp_files','')
            #     print(reseouceUrl)
            #     resources.append(reseouceUrl)

			# resources = []
            # res = tender.find_elements_by_tag_name('a')
            # for url in res:
            #     url = url.get_attribute('href')
            #     if('.pdf' in url or '.xls' in url or '.xlsx' in url or '.doc' in url):
            #         resources.append(url)
            #         print("Resource url: " +url)

			# title_en = tender.find_element_by_css_selector('td:nth-of-type(3) a').text.strip()
			# if('expression of interest' in title_en.lower() or 'eoi' in title_en.lower()):
			# 	tender_type = 'rei'
			# else:
			# 	tender_type = 'spn'
			# print('Title type = ' + tener_type)

			# try:
			# 	est_cost = re.findall(r'\d.*',est_cost)[0]
			# 	if ('.' in est_cost):
			# 		estimated_cost = str(float(est_cost)* 100000).split('.')[0]
			# 	else:
			# 		estimated_cost = str(int(est_cost)* 100000)
			# except:
			# 	estimated_cost = ''

			#ex = 'Get date in string'
			#date = datetime.strptime(ex, '%d/%m/%Y')
			#published_date = date.strftime('%Y/%m/%d')

			#ex = 'Get date in string'
			#date = datetime.strptime(ex, '%d/%m/%Y')
			#end_date = date.strftime('%Y/%m/%d')

			'''
			notice_text = ""

			notice_text += "Title: "
			notice_text += title_en
			notice_text += "</br>"

			notice_text += "Published Date: "
			notice_text += published_date
			notice_text += "</br>"

			notice_text += "Tender submission last date: "
			notice_text += end_date
			notice_text += "</br>"

			notice_text += "Status: "
			notice_text += status
			notice_text += "</br>"

			notice_text += "Attachment Doc: "
			notice_text += attachment_url

			notice_text += "</br></br>"

			

			NOTICE = ET.SubElement(NOTICES, "NOTICE")

			ET.SubElement(NOTICE, "LANG").text = "EN"
			ET.SubElement(NOTICE, "BUYER").text = ''
			ET.SubElement(NOTICE, "BUYER_ID").text = ''

			ET.SubElement(NOTICE, "PERFORMANCE_COUNTRY").text = ""
			ET.SubElement(NOTICE, "CITY_LOCALITY").text = ''

			ET.SubElement(NOTICE, "NOTICE_NO").text = reference
			ET.SubElement(NOTICE, "NOTICE_TITLE").text = title_en.title()
			ET.SubElement(NOTICE, "TYPE").text = ''
			ET.SubElement(NOTICE, "METHOD").text = ""

			ET.SubElement(NOTICE, "EST_COST").text = ''
			ET.SubElement(NOTICE, "CURRENCY").text = ""

			ET.SubElement(NOTICE, "PUBLISHED_DATE").text = published_date
			ET.SubElement(NOTICE, "END_DATE").text = end_date

			# ET.SubElement(NOTICE, "ORGANIZATION").text = organization
			ET.SubElement(NOTICE, "ADDRESS").text = ''
			ET.SubElement(NOTICE, "CONTACT_NAME").text = ''
			# ET.SubElement(NOTICE, "CONTACT_TITLE").text = ''
			ET.SubElement(NOTICE, "CONTACT_PHONE").text = ''
			ET.SubElement(NOTICE, "FAX").text = ''
			ET.SubElement(NOTICE, "WEBSITE").text = ''
			ET.SubElement(NOTICE, "CONTACT_EMAIL").text = ''
			ET.SubElement(NOTICE, "CITY").text = ''
			ET.SubElement(NOTICE, "COUNTRY").text = ""
			ET.SubElement(NOTICE, "NOTICE_TEXT").text = notice_text
			ET.SubElement(NOTICE, "RESOURCE_URL").text = resource
			# try:
			# 	for resource in resources:
			# 		ET.SubElement(NOTICE, "RESOURCE_URL").text = resource
			# except:
			# 	pass
			ET.SubElement(NOTICE, "ADMIN_URL").text = url

			Don't remove
			cpvs = classifier.get_cpvs(title_en.lower(), category)
			cpv_count = 0
			if (cpvs):
				for cpv in cpvs:
					if (cpv not in false_cpv):
						ET.SubElement(NOTICE, "CPV").text = str(cpv)
						cpv_count += 1
						try:
							print(cpv + ' - ' + cpv_dict[cpv].lstrip().strip())
						except:
							pass
			if (cpv_count != 0):
				ml_cpv += 1

			'''

			notice_count += 1
			print('.............................')



		if (notice_count != 0):
			print(notice_count)
			fn.xmlCreate('Folder', 'Internal Code', NOTICES, notice_count)
			# fn.session_log('Internal Code', notice_count, 0, ml_cpv, 'XML uploaded')
		#else:
			#fn.session_log('Internal Code', 0, 0, 0, 'No notices')

	

# Don't remove
except Exception as e:
	driver.save_screenshot('file_name.png')
	driver.quit()
	page.quit()
	# fn.xmlUpload('Folder', 'Internal Code', NOTICES, notice_count)
	# fn.error_log('Internal Code', e)
	# fn.session_log('internal_code', notice_count, 0, ml_cpv, 'Script error')
	raise e
