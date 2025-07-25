def analyze_header(header_text):
    result = {}

    # SPF check
    if "spf=pass" in header_text:
        result["SPF Result"] = "SPF passed"
    elif "spf=fail" in header_text:
        result["SPF Result"] = "SPF failed"
    else:
        result["SPF Result"] = "N/A"

    # DKIM check
    if "dkim=pass" in header_text:
        result["DKIM Result"] = "DKIM passed"
    elif "dkim=fail" in header_text:
        result["DKIM Result"] = "DKIM failed"
    else:
        result["DKIM Result"] = "N/A"

    # DMARC check
    if "dmarc=pass" in header_text:
        result["DMARC Result"] = "DMARC passed"
    elif "dmarc=fail" in header_text:
        result["DMARC Result"] = "DMARC failed"
    else:
        result["DMARC Result"] = "N/A"

    # Trace
    result["Mail Server Trace"] = "N/A"
    for line in header_text.splitlines():
        if line.startswith("Received: from"):
            result["Mail Server Trace"] = line.strip()
            break

    return result
