:- module miao.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
:- import_module int.
main(!IO) :- loop(10000, !IO).
:- pred loop(int::in, io::di, io::uo) is det.
loop(N, !IO) :- ( if N =< 0 then true else io.write_string("喵", !IO), loop(N - 1, !IO) ).
