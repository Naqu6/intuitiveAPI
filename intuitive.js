// Contact.js
// Copyright Ryan Ehrlich 2017

SUCCESS_RESULT = true
FAILURE_RESULT = false

UPSTREAM_MESSAGE = true
DOWNSTREAM_MESSAGE = false

api = {}

function contact(data) {
	$.ajax({
		dataType: "json",
		url: "/api",
		data: data,
		success: (result) => {
			if (result.result == SUCCESS_RESULT) {
				if (result.messageType == DOWNSTREAM_MESSAGE) {
					manageDownstreamMessage(result);
				}
			} else {
				console.error(result.errorText);
			}
		}
	});
}



function generateFunctions() {
	var apiEndpoints = [
		// BEGIN ENDPOINT INSERTION
		{"name": "endpoint", "argsKey": ["userId","password"]},
		{"name": "endpoint2", "argsKey": ["userId","password"]},
		// END ENDPOINT INSERTION
	];

	apiEndpoints.forEach((endpoint, _) => {
		api[endpoint.name] = () => {
			var apiArgs = {};

			for (var i = 0; i < arguments.length; i++) {
				apiArgs[endpoint.argsKeys[i]] = argument[i];
			}

			contact(apiArgs);
		};
	});
}