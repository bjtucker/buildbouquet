resource "github_branch_protection" "main" {
  repository_id = var.repository_id
  branch        = "main"

  required_status_checks {
    strict = true
    contexts = [
      "continuous-integration",
    ]
  }

  enforce_admins = true

  required_pull_request_reviews {
    require_code_owner_reviews = true
  }
}
