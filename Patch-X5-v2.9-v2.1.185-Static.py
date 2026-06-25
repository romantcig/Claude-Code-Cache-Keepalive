#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import hashlib
import shutil
import argparse
from pathlib import Path

# Pristine expected hash for standard claude.exe v2.1.185 build
TARGET_HASH = "28683edfedfc99e80aadd39599f3802827225f23648360493d723e95d8cafc0f"

PATCHES = [
    # GO7 IIFE (Read-A)
    (84228678, 350, b'${(()=>{let g=globalThis;if(g.__krS)return"";g.__krS=1;setInterval(()=>{try{if(g.__krI)return;let t=g.__krLast;if(t&&Date.now()-t<24e4)return;if(!Kgo)return;let a=Date.now()-Kgo;if(a<24e4||a>=3e5)return;g.__krI=1;X1t(new AbortController().signal).finally(()=>{g.__krI=0}).catch(()=>{})}catch(_){}},1e4).unref();return""})()/*PPPPPPPPPPPPPPPPPPPPXX*/}'),
    # GO7 IIFE (Read-B)
    (84229944, 570, b'${(()=>{let g=globalThis;if(g.__krS)return"";g.__krS=1;setInterval(()=>{try{if(g.__krI)return;let t=g.__krLast;if(t&&Date.now()-t<24e4)return;if(!Kgo)return;let a=Date.now()-Kgo;if(a<24e4||a>=3e5)return;g.__krI=1;X1t(new AbortController().signal).finally(()=>{g.__krI=0}).catch(()=>{})}catch(_){}},1e4).unref();return""})()/*PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP*/}'),
    # awaySummary 函数体
    (87796945, 858, b'async function X1t(e){let t=ele();if(!t)return{kind:"no-turn"};let n=new AbortController;e.addEventListener("abort",()=>n.abort(),{once:!0});try{let{messages:r,totalUsage:$u}=await Jk({promptMessages:[Rn({content:bqd})],cacheSafeParams:t,overrides:{abortController:n},canUseTool:async()=>({behavior:"deny",message:"Away summary cannot use tools",decisionReason:{type:"other",reason:"away_summary"}}),querySource:"away_summary",forkLabel:"away_summary",maxOutputTokens:1,maxTurns:1,skipCacheWrite:!0,skipTranscript:!0});if($u?.cache_read_input_tokens>0)Kgo=Date.now();if(e.aborted)return{kind:"aborted"};let o=r.find((i)=>i.type==="assistant"&&i.isApiErrorMessage);if(o)return{kind:"api-error",text:oaa([o],!0)};let s=oaa(r,!1);return s?{kind:"ok",text:s}:{kind:"failed"}}catch(r){if(e.aborted)return{kind:"aborted"};return{kind:"failed"}/*PPPPPPPPPPPPPPP*/}}'),
    # away_summary recovery 重试绕过
    (91567744, 281, b'if(IZa(ie,ot),PZa(Ie)){if(V<Tjp&&a!=="away_summary"){let Lr=Rn({content:"Output token limit hit. Resume directly \\u2014 no apology, no recap of what you were doing. "+"Pick up mid-thought if that is where the cut happened. Break remaining work ",isMeta:!0,now:p.now,uuidFn:p.uuid})'),
    # M8 活动感知注入 __krLast
    (91546920, 1004, b'if(R)globalThis.__krLast=Date.now();try{while(Ht){Ht=!1;let Ie=Cjp(ot,vt)||!ke.advisorModel||KRa(ot,ke.advisorModel)?ke.advisorModel:void 0;if(ke.advisorModel&&Ie===void 0)T(`[AdvisorTool] Skipping advisor - ${ke.advisorModel} cannot advise non-configured attempt model ${ot} (configured: ${vt})`);if(S!==void 0)if(v)S=void 0,v=!1;else v=!0;let pt=[],ut=ie.length,kt,Ut,mn=[],sr,Lr=!1;try{let nr=!1,qr=[],io=[],vs=QUi(),go=$e(Ktr()),Sn=M.getAppState().replBridgeSessionActive,On=vs||Sn,Ho=oJa({currentModel:ot,alreadyUsed:y,declined:_,suppressionAlreadyLogged:b,requestDialog:M.requestDialog,isMainThread:R,consumerLacksDialogCapability:On,sticky:N??_k()});if(Ho.shouldLogSuppression)b=!0,W("tengu_refusal_fallback_suppressed",{reason:M.requestDialog===void 0?Je("no_dialog_host_setting_off"):vs?Je("no_consumer_capability_setting_off"):Je("remote_controlled_session_setting_off"),capability_source:go});let wr=Ho.serverLane,Mt=dt;dt=void 0;let Wn=Pt;Pt=void 0;let _n=Bt;Bt=void 0;/*PPPPPPPPPPPPPPPPPPP*/'),
]

BACKUP_SUFFIX = ".x5patch-bak"

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def cmd_restore(target: Path) -> None:
    backup = target.with_name(target.name + BACKUP_SUFFIX)
    if not backup.exists():
        print(f"[FAIL] Backup file {backup.name} not found, nothing to restore.")
        sys.exit(1)
        
    backup_data = backup.read_bytes()
    try:
        target.write_bytes(backup_data)
        print(f"[OK] Restored original {target.name} from backup.")
    except PermissionError:
        print("exe in use, please close Claude Code first.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        prog="patch-x5-static",
        description="Static recap-keepalive patch for Claude Code v2.1.185",
    )
    parser.add_argument("--restore", action="store_true", help="Restore original exe from backup")
    args = parser.parse_args()

    target = Path.home() / ".local" / "bin" / "claude.exe"
    if not target.exists():
        print("claude.exe not found")
        sys.exit(1)

    if args.restore:
        cmd_restore(target)
        sys.exit(0)

    data = target.read_bytes()
    cur_hash = sha256_hex(data)
    
    if cur_hash != TARGET_HASH:
        # Check if already patched
        buf = bytearray(data)
        for off, length, repl in PATCHES:
            buf[off:off+length] = repl
        if sha256_hex(buf) == cur_hash:
            print("Already patched.")
            sys.exit(0)
        else:
            print(f"Hash mismatch. Expected v2.1.185 ({TARGET_HASH[:8]}), got {cur_hash[:8]}.")
            print("This static patch ONLY works on exactly v2.1.185.")
            sys.exit(1)

    backup = target.with_name(target.name + BACKUP_SUFFIX)
    if not backup.exists():
        shutil.copy2(target, backup)
        print(f"[backup] Backup created: {backup.name}")

    buf = bytearray(data)
    for off, length, repl in PATCHES:
        buf[off:off+length] = repl
        
    try:
        target.write_bytes(buf)
        print("[OK] Static patch applied.")
    except PermissionError:
        print("exe in use, please close Claude Code.")
        sys.exit(1)

if __name__ == "__main__":
    main()
