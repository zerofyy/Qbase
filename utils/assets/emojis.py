import pyemojify


class Emojis:
    """ Static class for custom Discord emojis. """

    blank = '<:ee:1105122910051508225>'

    check = '<:ee:1105122920159772784>'
    denied = '<:ee:1105122927554338960>'
    error = '<:ee:1105122928892334111>'
    warning = '<:ee:1105509639778467883>'
    info = '<:ee:1105509087896146071>'
    question = '<:ee:1105122980759081030>'
    slash = '<:ee:1105509426909171833>'

    ping_good = '<:ee:1105122977206517890>'
    ping_ok = '<:ee:1105509430415597649>'
    ping_bad = '<:ee:1105509319719534682>'

    archive = '<:ee:1105508991620087869>'
    bookmark = '<:ee:1105508994883264524>'
    time = '<:ee:1105509039443562577>'
    folder = '<:ee:1105509043444912208>'
    id = '<:ee:1105509085144682576>'
    link = '<:ee:1105509089129283634>'
    pen = '<:ee:1105509318247325736>'
    settings = '<:ee:1105509424140918815>'
    reload = '<:ee:1105509421494313090>'
    stats = '<:ee:1106243081344393267>'
    ticket = '<:ee:1105509554323734569>'
    upload = '<:ee:1105509544265797782>'
    delete = '<:ee:1105509564809490614>'
    user = '<:ee:1105509635408019527>'

    thumbsup = '<:ee:1105122994587697172>'
    thumbsdown = '<:ee:1105509548460089395>'

    circle_green = '<:ee:1118168053453176952>'
    circle_yellow = '<:ee:1118168057681039370>'
    circle_red = '<:ee:1118168055768436879>'
    circle_blue = '<:ee:1247260406565834793>'

    loading = '<a:ae:1105122960068579368>'

    # Convert :discord: emojis into actual emoji characters
    emojify = pyemojify.emojify


__all__ = ['Emojis']
