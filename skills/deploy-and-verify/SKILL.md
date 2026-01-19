---
name: deploy-and-verify
description: Full deployment workflow with version verification. Use when the user says "/deploy-and-verify", "deploy", "ship it", "push to production", or wants to deploy changes and verify they're live.
---

# Deploy and Verify

Deploy changes to production and verify the deployment succeeded by checking service logs.

## Workflow

### Phase 1: Pre-Deployment Checks

1. **Check git status** - Ensure working directory is clean or changes are committed
   ```bash
   git status
   git log --oneline -3
   ```

2. **Identify deployment scripts** - Look for scripts in the project's `/scripts/` directory:
   ```
   scripts/deploy/       # Deployment scripts
   scripts/infra/        # Infrastructure/verification scripts
   ```

3. **Identify services** - Common services to check:
   - **Vercel** (frontend) - Auto-deploys on push to main
   - **Railway** (workers) - Auto-deploys on push
   - **Supabase** (edge functions) - Manual deploy via CLI
   - **Other** - Check `docs/operations.md` or `README.md` for service list

### Phase 2: Deployment

1. **Push changes** (if not already pushed):
   ```bash
   git push origin main
   ```

2. **Run deployment scripts** (if they exist):
   ```bash
   # Check for and run any deploy scripts
   ./scripts/deploy/release.sh    # If exists
   # OR individual service deploys:
   vercel --prod                   # Manual Vercel deploy
   supabase functions deploy       # Supabase edge functions
   ```

### Phase 3: Verification (CRITICAL)

**ALWAYS verify deployments - never assume success.**

1. **Check Vercel deployment** (if applicable):
   ```bash
   # Check deployment status
   vercel ls --prod 2>/dev/null | head -5

   # Or check via API
   curl -s -o /dev/null -w "%{http_code}" https://<domain>/api/health
   ```

2. **Check Railway logs** (if applicable):
   ```bash
   railway logs --service <service-name> | tail -50
   # Look for: startup messages, errors, "ready" signals
   ```

3. **Check Supabase** (if applicable):
   ```bash
   supabase functions list
   # Check edge function logs in Supabase Dashboard
   ```

4. **Run verification scripts** (if they exist):
   ```bash
   ./scripts/deploy/verify-deployment.sh <url>
   ./scripts/infra/verify-prod-deployment.sh
   ```

5. **Health checks** - Common endpoints to verify:
   ```bash
   curl -s https://<domain>/api/health
   curl -s -o /dev/null -w "%{http_code}" https://<domain>
   ```

### Phase 4: Report Results

Provide a summary:

```
## Deployment Summary

**Status:** SUCCESS / PARTIAL / FAILED

### Services Deployed
| Service | Status | Notes |
|---------|--------|-------|
| Vercel (frontend) | ✅ Ready | https://example.com |
| Railway (worker) | ✅ Running | Logs show normal operation |
| Supabase (functions) | ⏭️ Skipped | No changes |

### Verification Results
- Health endpoint: 200 OK
- Landing page: ✅ Loads
- API routes: ✅ Responding

### Logs Checked
- Railway eligibility-worker: No errors, polling for jobs
- Vercel build: Completed in 45s

### Next Steps (if any issues)
- ...
```

## Service-Specific Commands

### Vercel
```bash
vercel ls                    # List deployments
vercel logs <url>           # View function logs
vercel --prod               # Force production deploy
```

### Railway
```bash
railway status              # Check status
railway logs                # View logs (live tail)
railway logs --service <name>  # Specific service logs
```

### Supabase
```bash
supabase functions list     # List functions
supabase functions deploy   # Deploy all functions
supabase db push           # Push migrations
```

## Finding Project-Specific Scripts

Always check for these directories first:
1. `scripts/deploy/` - Deployment scripts
2. `scripts/infra/` - Infrastructure and verification
3. `docs/operations.md` - Deployment documentation

Read any existing scripts to understand the project's deployment workflow before running generic commands.

## Error Handling

If deployment fails:
1. Check logs immediately for the failing service
2. Look for common issues:
   - Missing environment variables
   - Build failures
   - Network/connectivity issues
   - Database migration issues
3. Report the specific error and suggest fixes
4. Offer to rollback if needed:
   ```bash
   git revert HEAD
   git push origin main
   ```

## Important Notes

- **Never skip verification** - Always check logs after deployment
- **Check operations docs** - Read `docs/operations.md` if it exists for project-specific procedures
- **Multiple services** - Many projects deploy to multiple services (frontend + worker + functions)
- **Log interpretation** - Look for startup messages, errors, and "ready" indicators in logs
- **Health endpoints** - Most APIs have `/api/health` or similar endpoints to check
