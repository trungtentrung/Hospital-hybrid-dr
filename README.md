# Hospital Hybrid Cloud DR System

# Tổng quan dự án
Hệ thống Disaster Recovery hybrid cloud cho bệnh viện,
kết hợp Proxmox on-premise với AWS Cloud theo mô hình Pilot Light.

## Công nghệ sử dụng
# On-Premise
- Proxmox VE (3 node cluster: PVE-01, PVE-02, PVE-03)
- Ceph Storage (3x replication)
- Proxmox Backup Server (PBS)
- Veeam Backup
- Fortinet Firewall

# AWS Cloud
- AWS Elastic Disaster Recovery (DRS)
- CloudWatch (Monitoring + Alarm)
- Lambda (Automation)
- SNS (Notification)
- EC2 (Recovery Instance)
- Route 53 (DNS Failover)
- S3 (Storage)
- Amazon Relational Database Service (RDS)

# Cơ chế hoạt động
1. VM Proxmox liên tục replication data lên AWS DRS
2. Heartbeat script push metric lên CloudWatch mỗi 60 giây
3. CloudWatch Alarm phát hiện VM sập trong 2 phút
4. SNS trigger Lambda và Admin Mails tự động
5. Lambda kích hoạt DRS Recovery và cập nhật lại IP sang Route 53
6. EC2 Recovery Instance chạy lên trong 15-20 phút
7. RDS được Lambda kích hoạt lên Promote Replica to Master

# RPO & RTO
1. RPO < 2 phút
2. RTO 10-15 phút
