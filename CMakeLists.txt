cmake_minimum_required(VERSION 3.10)
project(brainrot-sniper-utility)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(brainrot_sniper main.cpp src/roblox_scanner.cpp src/script_sniper.cpp)
target_include_directories(brainrot_sniper PRIVATE include)
target_link_libraries(brainrot_sniper PRIVATE curl)