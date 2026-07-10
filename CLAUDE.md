# CLAUDE.md — Project Working Contract

> **Mission:** <_one-sentence statement of what this project is and why it exists. fill in per project._>

This file is the working contract for any agent — human or AI — that touches this
repository. **These rules override default behavior.** If a rule conflicts with a
convention read elsewhere, this file wins unless it explicitly defers.

This is a **template**. Replace every angle-bracket placeholder (`<_..._>`) with
the project's real values before the first commit. Delete any section that does
not apply, but do not weaken the doctrine to make a section fit — if a section
does not fit, the project probably needs a different shape.

---

## 1. The Inviolable Principles

These principles are non-negotiable. They apply to every language, every stack,
every commit.

1. **Zero Assumption** — No value is assumed. No constant, type, signature,
   protocol field, endpoint, flag, or environment variable is invented to make
   code compile or a test pass. If a value is unknown, it is left as a documented
   blocker (`/* FIXME: source needed */` or equivalent) and the code path is
   marked pending. A plausible placeholder is still a placeholder. Every constant
   must have a verifiable source: a spec, a standard, a capture, a disassembly, a
   log, a header, a contract. "Probably" is not a source.

2. **Evidence over Intuition** — Every behavioral claim — a constant, an offset,
   a return value, a side effect, an error code — must be traceable to evidence:
   a test that exercises it, a spec that states it, a standard that defines it, a
   capture that shows it, or a log that proves it. "I think it works that way" is
   not evidence. When evidence is missing, the claim is a blocker, not a fact.

3. **Safe by Default** — The unsafe configuration must not be representable in
   the API. Validation of inputs, bounds on buffers, handling of error returns,
   no unbounded copies, no unchecked casts, no silent swallowing of failures.
   Fail closed: if a guarantee cannot be verified, the operation is rejected. A
   missing check is a bug, not a TODO. The default posture is deny; permission is
   explicit and narrow.

4. **Non-Interference** — A component must not break what another component owns.
   A detector does not claim the resource it detects. A library does not mutate
   state it does not own. A test does not leave side effects for the next test. A
   migration does not lock out existing callers. If two components share a
   boundary, the contract at that boundary is explicit and guarded. Interference
   with a working system is a critical bug.

5. **Traceability (Immutable Nomenclature)** — Names that encode provenance are
   kept one-to-one with their source: a disassembly symbol, a standard field, a
   protocol tag, a spec identifier. They are not renamed to _v2, _New, _Fixed,
   _clean. Renaming severs the link to the evidence and is forbidden. Aesthetic
   preference does not override traceability.

6. **Extensible by Design** — Code is written for the 100th case, not just the
   first. Identifiers are centralized, access is indexed or dispatch-based, APIs
   are generic over the thing they operate on. Adding a new instance of the thing
   the project manages must not require touching a switch statement, a
   hand-rolled serializer, or a copy-pasted handler. If the third addition smells
   like duplication, the abstraction is extracted before the fourth.

**Separation doctrine:** pure logic — math, parsing, encoding, decisions, state
transitions — lives in functions with no I/O and no hidden state. This is the
directly testable surface. Orchestrators — the parts that read files, open
sockets, call frameworks, touch the clock, hit the network — only wire and call
the pure functions. Responsibilities are never mixed. If a function both
computes and talks to the outside world, split it.

---

## 2. Style and Conventions

- **Language and stack:** <_primary language, runtime/framework, and version.
  pin versions that matter._> This is a template; the project fills this in.
  Within a project, the stack is fixed — do not introduce a second language or
  framework mid-stream without a spec that justifies it.
- **Identifiers and strings in code: English.** Comments explain a non-obvious
  *why*, never the *what* the code already says. Documentation (specs, this file,
  README) may be in the team's working language.
- **Naming:** consistent prefix or namespace per module. No global mutable state
  without an explicit, lifecycle-managed singleton. Every acquisition (alloc,
  open, connect, lock) has a named, idempotent releaser.
- **Formatting:** whatever the project's formatter enforces, enforced
  automatically on save and on CI. No manual reformats mixed into logic commits.
- **Headers / interface definitions:** document the contract — inputs, outputs,
  errors, ownership, thread-safety — not the implementation.

---

## 3. Methodology: SDD + Strict TDD + BDD Given-When-Then

For every module, the cycle is inviolable and **in this order**, boyscout mode,
technical-debt extinguisher:

1. **Spec** — `spec/<module>.md`: inputs, outputs, error table, safety
   guarantees, what is explicitly out of scope, and — critically — the **source
   of every constant and assumption** (standard, capture, contract, disassembly).
   Written in Given-When-Then (BDD) form: *Given* a precondition, *When* an
   action, *Then* an observable outcome. The spec is the contract the tests
   enforce and the code fulfills.

2. **Test (red)** — `tests/test_<module>.<ext>` in the project's test framework.
   It must **fail** because no implementation exists yet. Tests target the pure
   functions first (unit, deterministic, no I/O) and the orchestrators second
   (integration, with I/O stubbed or sandboxed). A test that cannot fail is not a
   test — delete it or make it assert something real.

3. **Code (green)** — `src/<module>.<ext>` with the minimum code to pass the
   tests. **No compilable placeholders:** an unknown value is a documented
   blocker, never a fudged constant. If a test cannot be written because a value
   is unknown, the test is marked skip-with-reason and the blocker is recorded;
   the implementation does not pretend.

4. **Refactor** — harden pointers/bounds/ownership, improve legibility, extract
   duplication, without breaking tests. **Refactor is never out of scope.** If
   you see duplicated logic, unify it — this is imperative: seek duplicated logic
   and extinguish it without losing functionality. If you can do in 10 or 1 line
   what you did in 40, do it, as long as it respects the project's design
   principles and loses no functionality and adds no debt. Boyscout mode: if you
   see technical debt, extinguish it without breaking functionality. The same
   applies to security failures and vulnerabilities — their extinction is never
   out of scope.

5. **Validate** —
   - Unit + integration suite green.
   - Static analysis clean (whatever the project uses: linter, type checker,
     dependency scanner).
   - Dynamic analysis clean where applicable (sanitizers for memory/UB, leak
     checker, race detector). Zero leaks, zero UB, zero races before closing.
   - The project's golden/characterization test — the one canonical example
     every contributor knows — must pass. Always.

6. **Fuzz** — every path that takes external input is fuzzed: parsers,
   deserializers, protocol decoders, input validators. The fuzzer runs until it
   finds no crashes, no leaks, no undefined behavior, no assertion failures for a
   meaningful budget. Findings are fixed at the source, not by suppressing the
   fuzzer. New input-taking code ships with a fuzz target.

7. **Document** — **only after** validate and fuzz pass: update the spec, this
   `CLAUDE.md` (blocker resolved, new doctrine, new invariant), the README.
   Documenting before validating is documenting what is not yet true.

**Do not write implementation before spec and test.** Do not advance a phase
until the previous one is green, validated, and (where applicable) fuzzed.

**Test-driven design:** pure logic — math, parsing, encoding, decisions — lives
in pure functions with no I/O (the directly testable surface); orchestrators only
wire and call those pure functions. Design so that the interesting behavior is
the testable behavior.

---

## 4. Technology Stack

> This section is **the only project-specific part that must be filled in**.
> Everything else in this template is stack-neutral. Delete technologies that do
> not apply; add rows that do.

| Component | Technology | Note |
| :-- | :-- | :-- |
| <_component_> | <_language/framework/version_> | <_constraint or reason_> |
| Tests | <_framework_> | TDD. <_install/run command_>. |
| Static analysis | <_tool_> | CI gate. |
| Dynamic analysis | <_sanitizer/leak checker_> | <_command_>. |
| Fuzzing | <_fuzzer_> | <_command/targets_>. |
| Packaging | <_system_> | <_command_>. |

**The Makefile / build script is the single source of truth for commands.**
Wrapper scripts are thin delegators. If a wrapper duplicates build logic it
desynchronizes and becomes debt — unify.

### Hardening

List the compiler/runtime flags the project mandates (bounds checking, stack
protection, fortify, strict warnings-as-errors, etc.). If the language has no
such flags, state the static-analysis gate that substitutes for them.

### Critical blockers (values pending evidence)

Track here any value the project cannot yet source. Each entry: what is unknown,
why it matters, the method to resolve it (disassembly, capture, standard, log),
and the status. **No value in this list is ever filled with a guess.** When
resolved, move it to the resolved log with the evidence link.
```

---

## 5. Build, Hardening, and Verification

- **Build command:** &lt;_single command from the Makefile/build script_&gt;.
- **Test command:** &lt;_single command_&gt;.
- **Static analysis command:** &lt;_single command_&gt;.
- **Dynamic analysis command:** &lt;_single command_&gt;.
- **Fuzz command:** &lt;_single command_&gt;.

Every PR / integration must pass build + test + static analysis clean before
merge. Dynamic analysis and fuzzing are gates for paths that take external input.

The build file is the single source of truth for these commands. If you need a
new command, add it to the build file, not to a stray script.

---

## 6. Repository Structure

```
<_project_root_>/
├── CLAUDE.md                  # this file
├── <_build file_>             # single source of truth for commands
├── spec/                      # SDD specifications (Given-When-Then)
│   └── <module>.md
├── src/                       # implementations
│   └── <module>.<ext>
├── tests/                     # test suites
│   └── test_<module>.<ext>
├── docs/                      # additional documentation
└── <_other project dirs_>
```

&gt; Adapt to the project&#x27;s real layout. The invariant: spec, src, and tests live
&gt; as first-class siblings, each module present in all three.

---

## 7. Roadmap

&gt; **Status convention:** *closed* = spec + test green + static analysis clean +
&gt; dynamic analysis clean (where applicable) + fuzzed (where applicable). What
&gt; only compiles but could not be exercised is marked **pending validation**, not
&gt; verified.

### 7.1 Current status

| Component | Status | Evidence |
| :-- | :-- | :-- |
| &lt;_component_&gt; | &lt;_closed / pending / blocker_&gt; | &lt;_what proves the status_&gt; |

**Active doctrine decisions** (not evident in the code; do not re-litigate):

- **&lt;_doctrine name_&gt;:** &lt;_one-line statement and the reason it is
  non-negotiable_.&gt; See `[[_project-tag_]]`.

- Add one bullet per settled decision that a new contributor would otherwise
  re-open. If a decision is overturned, update the bullet — do not leave stale
  doctrine.

### 7.2 Closed milestones

- **&lt;_phase name_&gt;:** &lt;_what was delivered and what proves it. note if
  validation with real hardware/environment is still pending._&gt;

### 7.3 Roadmap — to cross

- **&lt;_next phase_&gt;:** &lt;_what unblocks it, what evidence is needed, what the
  validation criteria are._&gt;

**Ongoing background:** fuzzing of input paths; static/dynamic analysis hygiene;
documentation post-validation; continuous boyscout-mode debt extinction.

---

## 8. Rules for the Assistant (AI)

- Apply the full cycle of §3 **in order**: spec → red test → green code →
  refactor → validate (suite + static + dynamic) → fuzz → document. Do not skip
  steps, do not front-run implementation without spec + test, and do not
  document before validating and fuzzing.

- **Zero Assumption.** When a constant or contract is uncertain, ask for
  evidence with a directed question (inverse-Socratic: &quot;in the source of truth,
  go to X, follow the reference to Y, copy the value at Z&quot;). Never invent a
  value to unblock yourself.

- **Fail closed.** When a safety guarantee (bounds, pointer, ownership, I/O
  error) is in doubt, reject the operation; never weaken a guarantee for
  convenience. Missing validation is a bug, not a TODO.

- **Non-Interference.** A component does not break what another owns. Verify the
  boundary contract before touching a shared resource.

- **Immutable nomenclature.** Keep provenance-encoding names as they are. Do not
  rename &quot;to improve.&quot; Traceability is a requirement.

- Be honest about what is not verified: code that could not be exercised here
  (real I/O, hardware, network, production environment) is marked pending
  validation, not verified.

- Verify that every symbol, flag, and constant exists before recommending it
  (read the source, run the tool, check the standard). Do not rely on recall for
  specifics.

- New commands go in the **build file** (single source of truth), not in stray
  scripts that desynchronize (see §5).

- **Boyscout mode:** extinguishing technical debt and security failures is never
  out of scope, always without losing functionality. Seek and extinguish
  duplicated logic. If 40 lines can be 10 or 1 without losing functionality or
  adding debt, do it.

- **Lateral thinking** when the environment demands it (missing dependency,
  unsupported platform, unusual constraint). Document the non-obvious solution in
  the spec so the next agent does not re-derive it.

- When unsure between two approaches, prefer the one with the smaller blast
  radius and the more testable surface. State the trade-off; do not silently
  pick.
