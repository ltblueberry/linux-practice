# logging

## journald
Make journald logs persistent

```
sudo vim /etc/systemd/journald.conf
```
Change
```
[Journal]
Storage=persistent
```

![ps](screenshots/screenshot-journald-persistent.png)

Now logs will not disappear after the reboot.


Output format

![ps](screenshots/screenshot-journald-json.png)


Filter by log level

![ps](screenshots/screenshot-journald-level.png)


Filter by date and time

![ps](screenshots/screenshot-journald-filter-date.png)

![ps](screenshots/screenshot-journald-filter-ago.png)





