## S3

#### ls - List the buckets & it's objects

```
aws s3 ls
aws s3 ls s3://datatechdemo2222
aws s3 ls s3://datatechdemo2222 --recursive
aws s3 ls s3://datatechdemo2222 --recursive  --human-readable --summarize

```

#### cp - Copy command

```
aws s3 cp getdata.php s3://datatechdemo222
aws s3 cp /local/dir/data s3://datatechdemo222 --recursive
aws s3 cp s3://datatechdemo222/getdata.php /local/dir/data
aws s3 cp s3://datatechdemo222/ /local/dir/data --recursive
aws s3 cp s3://datatechdemo222/init.xml s3://backup-bucket
aws s3 cp s3://datatechdemo222 s3://backup-bucket --recursive
```

#### mv - Move command
```
aws s3 mv source.json s3://datatechdemo222
aws s3 mv s3://datatechdemo222/getdata.php /home/project
aws s3 mv s3://datatechdemo222/source.json s3://backup-bucket
aws s3 mv /local/dir/data s3://datatechdemo222/data --recursive
aws s3 mv s3://datatechdemo222 s3://backup-bucket --recursive
```

#### rm - remove command

```
aws s3 rm s3://datatechdemo222/queries.txt
aws s3 rm s3://datatechdemo222 --recursive

```

#### sync - synchronization commands

```
aws s3 sync backup s3://datatechdemo222
aws s3 sync s3://datatechdemo222/backup /tmp/backup
aws s3 sync s3://datatechdemo222 s3://backup-bucket
```

#### Create New S3 Bucket

```
aws s3 mb s3://datatechdemo222
aws s3 mb s3://datatechdemo222 --region us-west-2

```

#### Remove existing s3 bucket 

```
aws s3 rb s3://datatechdemo222

```

