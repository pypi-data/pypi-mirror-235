

'''
plan:

import prevail

prevail.abundantly ({
	"build": [{
		"kind": "header"
	}]
})

'''

import prevail.kinds.header as HEADER
import prevail.kinds.company as COMPANY

from flask import Flask

def abundantly (OBJECT):
	BUILDS = OBJECT ["build"]
	
	HTML = {
		"START": (
"""
<html>
<head></head>
<body>
<style>
h1, h2, h3, p, ul, li {
	margin: 0;
	padding: 0;
}

ul {
	padding-left: 20px;
}
</style>

"""),
		"MAIN": "",
		"END": (
"""
</body>
""")
	}
	
	
	

	for BUILD in BUILDS:
		KIND = BUILD ["kind"]
		
		if (KIND == "header"):
			HTML["MAIN"] += HEADER.BUILD (BUILD)
		
		elif (KIND == "company"):
			HTML["MAIN"] += COMPANY.INTRODUCE (BUILD)
		
		elif (KIND == "academics"):
			pass;
			
		else:
			print (f'Kind "{ KIND }" is not an option.')
			exit ()

	HTML_STRING = HTML ["START"] + HTML ["MAIN"] + HTML["END"]

	print (HTML_STRING)
	
	

	app = Flask (__name__)
	@app.route ("/")
	def hello_world():
		return HTML_STRING

	app.run(debug=True)

	return;