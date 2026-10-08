rule T1-Dangerous-Exec-Primitives {
  meta:
    description = "Primitive dangerous execution primitives (eval, exec, subprocess, os.system)"
    tier = "T1"
    confidence = "medium"
    artifact_class = "execution-primitive"
  strings:
    $eval = "eval(" nocase
    $exec = "exec(" nocase
    $subprocess = "subprocess" nocase
    $ossystem = "os.system" nocase
    $shell_true = "shell=True" nocase
  condition:
    any of them
}

rule T1-Hardcoded-Secret {
  meta:
    description = "Primitive hardcoded secret assignments (password, api_key, aws key prefix)"
    tier = "T1"
    confidence = "low"
    artifact_class = "hardcoded-secret"
  strings:
    $password = "password" nocase
    $api_key = "api_key" nocase
    $aws = "AKIA" nocase
  condition:
    any of them
}

rule T2-Shell-Plus-Network {
  meta:
    description = "Behavioral co-occurrence of shell execution with network exfiltration"
    tier = "T2"
    confidence = "high"
    artifact_class = "shell-network-cooccurrence"
  strings:
    $shell = "subprocess" nocase
    $curl = "curl" nocase
    $wget = "wget" nocase
    $socket = "socket" nocase
    $requests = "requests" nocase
  condition:
    2 of ($shell, $curl, $wget, $socket, $requests)
}

rule T2-Eval-Plus-Obfuscation {
  meta:
    description = "Eval/exec combined with encoding or obfuscation helpers"
    tier = "T2"
    confidence = "high"
    artifact_class = "eval-obfuscation"
  strings:
    $eval = "eval(" nocase
    $exec = "exec(" nocase
    $b64 = "base64" nocase
    $marshal = "marshal" nocase
    $decode = "decode(" nocase
  condition:
    ($eval or $exec) and ($b64 or $marshal or $decode)
}

rule T3-Project-Dangerous-Bridge {
  meta:
    description = "Project-specific rule: shell execution primitives bridged with network imports"
    tier = "T3"
    confidence = 70
    artifact_class = "project-dangerous-bridge"
  strings:
    $imports = "imports:" nocase
    $shell = "subprocess" nocase
    $sock = "socket" nocase
    $eval = "eval(" nocase
  condition:
    $imports and 2 of ($shell, $sock, $eval)
}
