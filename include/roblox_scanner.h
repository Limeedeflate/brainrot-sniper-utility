#ifndef ROBLOX_SCANNER_H
#define ROBLOX_SCANNER_H

#include <string>
#include <vector>

class RobloxScanner {
public:
    std::vector<std::string> scan_for_brainrot_scripts(const std::string& game_id);
};

#endif