#include "roblox_scanner.h"
#include <cassert>

void test_scan_for_brainrot_scripts() {
    RobloxScanner scanner;
    auto scripts = scanner.scan_for_brainrot_scripts("12345");
    assert(!scripts.empty());
}

int main() {
    test_scan_for_brainrot_scripts();
    return 0;
}