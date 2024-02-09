class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input()

    if email == "End":
        break

    if not "@" in email:
        raise MustContainAtSymbolError("Email must conatain @")
    
    tokens = email.split("@")
    domains = tokens[1].split(".")

    if len(tokens[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 charecters")
    
    if domains[1] not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

print("Email is valid")