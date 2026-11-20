#!/usr/bin/env escript
%% coding: utf-8
main(_) -> io:put_chars(unicode:characters_to_binary(lists:duplicate(10000, $喵))).
