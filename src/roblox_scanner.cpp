#include "roblox_scanner.h"
#include <curl/curl.h>
#include <sstream>

size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output) {
    size_t total_size = size * nmemb;
    output->append((char*)contents, total_size);
    return total_size;
}

std::vector<std::string> RobloxScanner::scan_for_brainrot_scripts(const std::string& game_id) {
    CURL* curl = curl_easy_init();
    std::vector<std::string> scripts;

    if (curl) {
        std::string readBuffer;
        std::string url = "https://www.roblox.com/games/" + game_id + "/script-dump";
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        // Simple parsing (mock implementation)
        if (readBuffer.find("brainrot") != std::string::npos) {
            scripts.push_back("https://roblox.com/script/" + game_id + "/brainrot");
        }
    }
    return scripts;
}