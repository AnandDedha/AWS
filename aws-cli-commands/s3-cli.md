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
aws s3 cp getdata.php s3://tgsbucket
aws s3 cp /local/dir/data s3://tgsbucket --recursive
aws s3 cp s3://tgsbucket/getdata.php /local/dir/data
aws s3 cp s3://tgsbucket/ /local/dir/data --recursive
aws s3 cp s3://tgsbucket/init.xml s3://backup-bucket
aws s3 cp s3://tgsbucket s3://backup-bucket --recursive
```

#### mv - Move command
```
aws s3 mv source.json s3://tgsbucket
aws s3 mv s3://tgsbucket/getdata.php /home/project
aws s3 mv s3://tgsbucket/source.json s3://backup-bucket
aws s3 mv /local/dir/data s3://tgsbucket/data --recursive
aws s3 mv s3://tgsbucket s3://backup-bucket --recursive
```

#### rm - remove command

```
aws s3 rm s3://tgsbucket/queries.txt
aws s3 rm s3://tgsbucket --recursive

```

#### sync - synchronization commands

```
aws s3 sync backup s3://tgsbucket
aws s3 sync s3://tgsbucket/backup /tmp/backup
aws s3 sync s3://tgsbucket s3://backup-bucket
```

#### Create New S3 Bucket

```
aws s3 mb s3://tgsbucket
aws s3 mb s3://tgsbucket --region us-west-2

```

#### Remove existing s3 bucket 

```
aws s3 rb s3://tgsbucket

```

