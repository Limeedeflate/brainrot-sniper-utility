#include "script_sniper.h"
#include <curl/curl.h>
#include <iostream>

bool ScriptSniper::snipe_script(const std::string& script_url) {
    CURL* curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, script_url.c_str());
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        return res == CURLE_OK;
    }
    return false;
}