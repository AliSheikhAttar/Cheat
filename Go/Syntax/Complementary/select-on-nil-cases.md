1. **Technically, on Paper**:
   - The `select` statement doesn’t “ignore” or skip cases with `nil` channels during its evaluation. It looks at every case, including those with `nil` channels, to see if any are ready.
   - So, it’s waiting for all cases to potentially become ready, `nil` or not.

2. **In Reality**:
   - A case with a `nil` channel can never be ready because its operation (send or receive) blocks forever.
   - As a result, `select` will never pick a `nil` channel case unless there are no other options—and even then, it can’t, because “no options” means blocking.
   - When there are non-`nil` channels, `select` ends up waiting only for those to become ready, since they’re the only ones that can unblock it.

3. **The Practical Outcome**:
   - If you have a mix of `nil` and non-`nil` channels, `select` effectively waits only for the non-`nil` cases, because the `nil` ones are perpetual non-starters.
   - Saying it “ignores” the `nil` cases is a shorthand for this: it doesn’t skip them in the code, but their inability to proceed means they don’t affect the outcome.

### Final Clarification
- **Does it jump to non-`nil` cases and wait only for them?** Not quite—it evaluates all cases, but the `nil` ones are dead weight.
- **Does it wait for all, but only non-`nil` matter in reality?** Yes, exactly! On paper, it’s waiting for any case to be ready; in practice, only non-`nil` cases can ever succeed, so that’s all it’s effectively waiting for when they’re present.

So, you’re spot on with your intuition: it waits for all cases “in theory,” but since `nil` channels block forever, it “really just waits for not `nil` cases in reality.” That’s the perfect way to sum it up!