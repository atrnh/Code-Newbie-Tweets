import os
from util.colors import colors

base_path = os.getcwd()
secrets_path = "{}/secret".format(base_path)

print("Creating directories:")
try:
    os.mkdir(secrets_path)
except OSError:
    print(colors.WARNING +
          "    {} already exists".format(secrets_path) +
          colors.ENDC
          )
else:
    print(colors.OKGREEN +
          "    Created {}".format(secrets_path) +
          colors.ENDC
          )

print("\nSetting up files in /secret:")
open("{}/__init__.py".format(secrets_path), "a").close()
print(colors.OKGREEN +
      "    Created {}/__init__.py".format(secrets_path) +
      colors.ENDC)

with open("{}/keys.py".format(secrets_path), "a") as secrets:
    with open("{}/util/secretkeys_template.py".format(base_path)) as template:
        secrets.write(template.read())
print(colors.OKGREEN +
      "    Created {}/keys.py".format(secrets_path) +
      colors.ENDC
      )

print("\nPLEASE POPULATE secret/keys.py WITH YOUR REDDIT API CREDENTIALS")

