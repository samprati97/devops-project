output "jenkins_public_ip" {
  value = aws_instance.jenkins_server.public_ip
}

output "eks_cluster_name" {
  value = module.eks.cluster_name
}

output "rds_endpoint" {
  value = aws_db_instance.rds.endpoint
}
