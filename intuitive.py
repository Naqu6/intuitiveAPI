#!/usr/bin/python
import endpoints

ENDPOINTS_START = "// **BEGIN ENDPOINT INSERTION**"
ENDPOINTS_END = "// **END ENDPOINT INSERTION**"

def updateJSAPI():
	with open("intuitive.js", "r+") as f:
		fileText = f.read()

	endpointsText = ENDPOINTS_START + "\n"

	for endpoint in endpoints.endpoints:
		endpointsText += """\t\t{"name": "%s", "argsKey": [%s]},\n""" % (endpoint[0], ",".join(['"%s"' % i for i in endpoint[1]]))

	endpointsText += "\t\t" + ENDPOINTS_END
	fileText = fileText.replace(ENDPOINTS_START + "\n\n\t\t" + ENDPOINTS_END, endpointsText)

	print fileText

if __name__ == "__main__":
	updateJSAPI()