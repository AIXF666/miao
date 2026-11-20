string(REPEAT "喵" 10000 MIAO)
execute_process(COMMAND "${CMAKE_COMMAND}" -E echo_append "${MIAO}")
