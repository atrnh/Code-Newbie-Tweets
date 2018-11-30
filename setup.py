# -*- coding: utf-8 -*-

import os
from util.cprint import cprint


base_path = os.getcwd()
secrets_path = "{}/secrets".format(base_path)
init_path = "{}/__init__.py".format(secrets_path)


# Set up the secret module
cprint("🚚 Creating directories...")
try:
    os.mkdir(secrets_path)
except FileExistsError:
    cprint("{} already exists".format(secrets_path),
           "yellow",
           "bold",
           indent=1,
           )
else:
    cprint("Created {}".format(secrets_path),
           "blue",
           indent=1,
           )

print("\n🚚 Creating a secret module...")

try:
    open(init_path).close()
except FileNotFoundError:
    open(init_path, "a").close()
else:
    with open(init_path, "w") as f:
        f.write("")

cprint("Created {}/__init__.py".format(secrets_path),
       "blue",
       indent=1,
       )


# Helper script for setting up:
# - Flask secret key
# - Reddit credentials
did_generate_key = False
keys_str = []
should_make_flask_key = input("\nGenerate a Flask key? (y/n) ")
key = "''"  # default blank key


try:
    assert should_make_flask_key == "y" or should_make_flask_key == "n"
except AssertionError:
    cprint("Unknown command. Skip generating a Flask key.", "red")
else:
    if should_make_flask_key == "y":
        print("Generating a random Flask key:")

        key = os.urandom(45)
        did_generate_key = True

        cprint("Key: {}".format(key.decode("utf-8", "replace")),
               "blue",
               indent=1,
               )

keys_str.append("    'flask_key': {},".format(key))

did_setup_creds = False
should_config = input("\nConfigure API credentials now? (y/n) ")
client_id = ""
user_secret = ""
try:
    assert should_config == "y" or should_config == "n"
except AssertionError:
    cprint("Unknown command. Skip configuring API credentials.", "red")
else:
    if should_config == "y":
        client_id = input("Client ID: ")
        user_secret = input("User secret: ")

        did_setup_creds = True

    else:
        cprint("Credentials were not configured", "yellow", "bold")

keys_str.append("    'client_id': '{}',".format(client_id))
keys_str.append("    'user_secret': '{}',".format(user_secret))

try:
    with open(init_path, "a") as k:
        with open("{}/util/secrets_template".format(base_path)) as t:
            k.write(t.read())
        k.write("\n".join(keys_str))
        k.write("\n}")

except FileNotFoundError:
    cprint("An error occurred while attempting to save your credentials",
           "red",
           "bold",
           )
    did_generate_key = False
    did_setup_creds = False

print()
if did_generate_key:
    cprint("✅ You generated a Flask key", "green")
else:
    cprint("❌ You did not generate a Flask key")

if did_setup_creds:
    cprint("✅ You set up your API credentials", "green")
else:
    cprint("❌ You did not set up your API credentials")

