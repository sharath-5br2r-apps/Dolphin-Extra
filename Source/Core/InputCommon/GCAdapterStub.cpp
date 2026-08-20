// Copyright 2026 Dolphin Emulator Project
// SPDX-License-Identifier: GPL-2.0-or-later

#include "InputCommon/GCAdapter.h"

#include "InputCommon/GCPadStatus.h"

namespace GCAdapter
{
void Init() {}
void ResetRumble() {}
void Shutdown() {}
void SetAdapterCallback(std::function<void(void)>) {}
GCPadStatus Input(int) { return {}; }
void Output(int, u8) {}
bool IsDetected(const char** error_message)
{
  if (error_message)
    *error_message = nullptr;
  return false;
}
bool DeviceConnected(int) { return false; }
void ResetDeviceType(int) {}
double GetCurrentPollRate() { return 0.0; }
}  // namespace GCAdapter
