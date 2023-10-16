set(NUREX_BENCH 
    ola
    )

foreach(entry ${NUREX_BENCH})
    add_executable(${entry} ${entry}.cpp)
    target_link_libraries(${entry} nurex)
endforeach(entry in ${NUREX_TESTS})
