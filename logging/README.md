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
```
sudo journalctl -u nginx -o json-pretty
```

![ps](screenshots/screenshot-journald-json.png)


Filter by log level
```
sudo journalctl -p crit
sudo journalctl -p info
```

![ps](screenshots/screenshot-journald-level.png)


Filter by date and time
```
sudo journalctl --since "2020-11-05 10:00" --until "2020-11-05 20:00"
sudo journalctl --since "10 minutes ago"
```

![ps](screenshots/screenshot-journald-filter-date.png)

![ps](screenshots/screenshot-journald-filter-ago.png)





