(ns miao)
(.write (.-stdout js/process) (apply str (repeat 10000 "喵")))
