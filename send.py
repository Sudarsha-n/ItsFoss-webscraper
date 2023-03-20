import get_content
import bot


def send():
    count = 0
    p = []
    with open("logs.txt", "r") as file:
        p = file.readlines()

    x = get_content.give_des()
    final = list(x[0].keys())
    for i in range(len(final)):
        if str(x[1][i]+"\n") in p or str(x[1][i]) in p:
                continue
        message = f"__**Headlines for Today!**__\n**{final[i]}**\n\n"
        for f in x[0][final[i]]:
            f = str(f).replace("<p>", "").replace("</p>", "").replace("</a>", "")
            if "<strong>" in str(f):
                f = str(f).replace("<strong>", "**").replace("</strong>", "**")
            if "<a" in str(f):
                f = str(f).replace(str(f)[str(f).index("<a") : str(f).index(">")], "")
            if "<em>" in str(f):
                f = str(f).replace("<em>", "*").replace("</em>", "*")
            if "<code>" in str(f):
                f = str(f).replace("<code>", "`").replace("</code>", "`")
            if "<br>" in str(f):
                f = str(f).replace("<br>", "\n")
            if "<br/>" in str(f):
                f = str(f).replace("<br/>", "\n")
            message += f"{f}\n"
        message += f"\nRead more at: {x[1][i]}"
        with open("logs.txt", "a") as file:
            file.write(f"\n{x[1][i]}")
        bot.bot_send(message=message)
        count += 1
    return count