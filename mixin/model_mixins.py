class ApiModel:
    def get_json(self):
        """Get me some JSON"""

        public_attrs = [attr for attr in dir(self) if not attr.startswith('_')]
        self_dict = {attr: getattr(self, attr) for attr in public_attrs}

        for key, val in self_dict.items():
            if isinstance(val, self):
                self_dict[key] = val.get_json()

        return json.dumps(self_dict)




