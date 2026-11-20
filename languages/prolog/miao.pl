:- initialization(main, main).
main :- set_stream(user_output, encoding(utf8)), forall(between(1, 10000, _), write('喵')).
