url = (input("informe a url: "))

if url.startswith("https://") and url.endswith(".com"):
    print("url valida")
else:
    print("url invalida")