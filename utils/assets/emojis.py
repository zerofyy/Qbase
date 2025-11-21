import pyemojify


class Emojis:
    """ Static class for custom Discord emojis. """

    blank = '<:blank:1441502114252591144>'

    check = '<:check:1441502121982824528>'
    denied = '<:denied:1441502130937794798>'
    error = '<:error:1441502132397408316>'
    warning = '<:warning:1441502200982405120>'
    info = '<:info:1441502150977913076>'
    question = '<:question:1441502179000189071>'
    slash = '<:slash:1441502188236181606>'

    ping_good = '<:pinggood:1441502176298926293>'
    ping_ok = '<:pingok:1441502177750421625>'
    ping_bad = '<:pingbad:1441502175108010165>'

    note = '<:note:1441502172654338171>'
    archive = '<:archive:1441502100629491772>'
    bookmark = '<:bookmark:1441502115980775519>'
    time = '<:clock:1441502128685449439>'
    folder = '<:folder:1441502133718614018>'
    id = '<:id:1441502149409247374>'
    link = '<:link:1441502153733701773>'
    pen = '<:pen:1441502173908435064>'
    settings = '<:settings:1441502181088956478>'
    reload = '<:reload:1441502180166209676>'
    stats = '<:stats:1441502190832193656>'
    ticket = '<:ticket:1441502194519118032>'
    upload = '<:upload:1441502198319026186>'
    delete = '<:delete:1441502195844644965>'
    user = '<:user:1441502199594356807>'

    thumbsup = '<:thumbsup:1441502193218748547>'
    thumbsdown = '<:thumbsdown:1441502191893348417>'

    circle_green = '<:circle_green:1441502124566384681>'
    circle_yellow = '<:circle_yellow:1441502127343140936>'
    circle_red = '<:circle_red:1441502125820608747>'
    circle_blue = '<:circle_blue:1441502123283058858>'

    loading = '<a:loading:1441502163967803604>'

    # Convert :discord: emojis into actual emoji characters
    emojify = pyemojify.emojify


__all__ = ['Emojis']
