from marshmallow.fields import Integer


###########################
# Custom Marshmallow fields

class NullableInteger(Integer):
    def _format_num(self, value):
        """Return the number value for value, given this field's `num_type`."""
        if value is None or value == '':
            return None
        return self.num_type(value)

####################
# Validation errors


class DataValidationError(Exception):
    """Raised if data validation error occurs during deserialization."""

    pass


class ChamberRequiredError(Exception):
    """Raised when chamber is required and not present."""

    pass


class InvalidChamber(Exception):
    """Raised when chamber is invalid."""

    pass
