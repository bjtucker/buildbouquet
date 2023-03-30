resource "github_branch_protection" "main" {
  repository_id = data.github_repository.current.id
  pattern       = "main"

  lifecycle {
    create_before_destroy = true
  }

  ignore_changes = [
    required_pull_request_reviews,
  ]
}
