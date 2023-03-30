resource "github_branch_protection" "main" {
  repository_id = data.github_repository.current.id
  pattern       = "main"

  enforce_admins = true

  lifecycle {
    create_before_destroy = true
  }

  ignore_changes = [
    enforce_admins,
    required_pull_request_reviews,
  ]
}
