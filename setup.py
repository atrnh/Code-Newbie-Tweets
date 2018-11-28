import os
from util.cprint import cprint

base_path = os.getcwd()
secrets_path = "{}/secrets".format(base_path)

# Setup the secret module
print("Creating directories:")
try:
    os.mkdir(secrets_path)
except FileExistsError:
    cprint("{} already exists".format(secrets_path),
           "WARNING",
           "BOLD",
           indent=1,
           )
else:
    cprint("Created {}".format(secrets_path),
           "OKBLUE",
           indent=1,
           )

print("\nSetting up files in /secret:")

init_path = "{}/__init__.py".format(secrets_path)
try:
    open(init_path).close()
except FileNotFoundError:
    open(init_path, "a").close()
else:
    with open(init_path, "w") as f:
        f.write("")

cprint("Created {}/__init__.py".format(secrets_path),
       "OKBLUE",
       indent=1,
       )

# Helper script for setting up:
# - Flask secret key
# - Reddit credentials
keys_str = []
should_make_flask_key = input("\nGenerate a Flask key? (y/n) ")
key = "''"  # default blank key

try:
    assert should_make_flask_key == "y" or should_make_flask_key == "n"
except AssertionError:
    cprint("Unknown command. Skip generating a Flask key.", "FAIL")
else:
    if should_make_flask_key == "y":
        print("Generating a random Flask key:")

        key = os.urandom(45)

        cprint("Key: {}".format(key.decode("utf-8", "replace")),
               "OKBLUE",
               indent=1,
               )

keys_str.append("    'flask_key': {},".format(key))

should_config = input("\nConfigure API credentials now? (y/n) ")
client_id = ""
user_secret = ""
try:
    assert should_config == "y" or should_config == "n"
except AssertionError:
    cprint("Unknown command. Skip configuring API credentials.", "FAIL")
else:
    if should_config == "y":
        client_id = input("Client ID: ")

        user_secret = input("User secret: ")

    else:
        cprint("Credentials were not configured", "WARNING")

keys_str.append("    'client_id': '{}',".format(client_id))
keys_str.append("    'user_secret': '{}',".format(user_secret))

try:
    with open(init_path, "a") as k:
        with open("{}/util/secrets_template".format(base_path)) as t:
            k.write(t.read())
        k.write("\n".join(keys_str))
        k.write("\n}")

    cprint("\nYour credentials have been saved to {}!".format(init_path),
           "OKGREEN",
           )
except FileNotFoundError:
    cprint("An error occurred while attempting to save your credentials",
           "FAIL",
           )
