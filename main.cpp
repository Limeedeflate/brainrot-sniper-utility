#include <iostream>
#include "roblox_scanner.h"
#include "script_sniper.h"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <roblox-game-id>" << std::endl;
        return 1;
    }

    RobloxScanner scanner;
    ScriptSniper sniper;

    auto scripts = scanner.scan_for_brainrot_scripts(argv[1]);
    for (const auto& script : scripts) {
        if (sniper.snipe_script(script)) {
            std::cout << "Successfully sniped: " << script << std::endl;
        } else {
            std::cerr << "Failed to snipe: " << script << std::endl;
        }
    }

    return 0;
}