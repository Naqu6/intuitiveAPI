#!/usr/bin/python
import endpoints
import re

ENDPOINTS_START = r"// BEGIN ENDPOINT INSERTION"
ENDPOINTS_END = "// END ENDPOINT INSERTION"

def updateJSAPI():
	with open("intuitive.js", "r") as f:
		fileText = f.read()

	endpointsText = ENDPOINTS_START + "\n"

	for endpoint in endpoints.endpoints:
		endpointsText += """\t\t{"name": "%s", "argsKey": [%s]},\n""" % (endpoint[0], ",".join(['"%s"' % i for i in endpoint[1]]))

	endpointsText += "\t\t" + ENDPOINTS_END
	fileText = re.sub(ENDPOINTS_START + r".*?" + ENDPOINTS_END, endpointsText, fileText,flags=re.DOTALL)

	with open("intuitive.js", "w") as f:
		f.write(fileText)

if __name__ == "__main__":
	updateJSAPI()