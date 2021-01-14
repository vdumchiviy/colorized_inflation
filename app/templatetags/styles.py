from django import template

register = template.Library()


@register.filter
def colorization(value, column):
    result = "white"
    if column == 13:
        result = "gray"
    elif column != 0:

        try:
            if float(value) < 0:
                result = "green"
            elif float(value) >= 1 and float(value) < 2:
                result = "lightpink"
            elif float(value) >= 2 and float(value) < 5:
                result = "lightcoral"
            elif float(value) > 5:
                result = "red"
        except:
            pass
    return result
