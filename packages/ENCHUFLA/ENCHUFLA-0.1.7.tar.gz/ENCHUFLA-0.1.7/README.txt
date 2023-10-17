


<h1>options</h1>

<b>installation</b>

<code>pip install ENCHUFLA
# pip install ENCHUFLA --upgrade
</code>

<b>start</b>
<code>ENCHUFLA KEG TAP --port 1110</code>


<b>build private key</b>
<code>import requests
import json
from os.path import dirname, join, normpath
import os
r = requests.put (
	'http://127.0.0.1:1110', 
	data = json.dumps ({
		"START": "BUILD ED448 PRIVATE KEY",
		"FIELDS": {
			"SEED": "5986888b11358bf3d541b41eea5daece1c6eff64130a45fc8b9ca48f3e0e02463c99c5aedc8a847686d669b7d547c18fe448fc5111ca88f4e8",
			"PATH": normpath (join (os.getcwd (), "ED448_PRIVATE_KEY.DER"))
		}
	})
)
print (r.text)
</code>


<b>build public key</b>
<code>import requests
import json
from os.path import dirname, join, normpath
import os
r = requests.put (
	'http://127.0.0.1:1110', 
	data = json.dumps ({
		"START": "BUILD ED448 PUBLIC KEY",
		"FIELDS": {
			"PRIVATE KEY PATH": normpath (join (os.getcwd (), "ED448_PRIVATE_KEY.DER")),
			"PUBLIC KEY PATH": normpath (join (os.getcwd (), "ED448_PUBLIC_KEY.DER")),
			"PUBLIC KEY FORMAT": "DER"
		}
	})
)
print (r.text)
</code>



<b>SIGN</b>
<code>import requests
import json
from os.path import dirname, join, normpath
import os
r = requests.put (
	'http://127.0.0.1:1110', 
	data = json.dumps ({
		"START": "ED448 SIGN",
		"FIELDS": {
			"PRIVATE KEY PATH": normpath (join (os.getcwd (), "ED448_PRIVATE_KEY.DER")),
			"UNSIGNED BYTES PATH": normpath (join (os.getcwd (), "UNSIGNED.UTF8")),
			"SIGNED BYTES PATH": normpath (join (os.getcwd (), "SIGNED.BYTES")),
		}
	})
)
print (r.text)
</code>

<b>VERIFY</b>
<code>import requests
import json
from os.path import dirname, join, normpath
import os
r = requests.put (
	'http://127.0.0.1:1110', 
	data = json.dumps ({
		"START": "ED448 VERIFY",
		"FIELDS": {
			"PUBLIC KEY PATH": normpath (join (os.getcwd (), "ED448_PUBLIC_KEY.DER")),
			"UNSIGNED BYTES PATH": normpath (join (os.getcwd (), "UNSIGNED.UTF8")),
			"SIGNED BYTES PATH": normpath (join (os.getcwd (), "SIGNED.BYTES")),
		}
	})
)
print (r.text)
</code>
