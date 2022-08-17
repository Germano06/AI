login:-getdata(U,P),write("login successfull"),nl.
login:-write("Login unsuccessfull, try again"),nl,login.
getdata(U,P):-write("Enter username"),nl,read(U),nl,write("Enter password"),nl,read(P),nl,user(U,P).
user(deepa,abc).
user(maya,xyz).