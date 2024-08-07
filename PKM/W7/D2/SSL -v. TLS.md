|term|def|
|-|-|
| SSL | Secure Sockets Layer |
| TLS | Transport Layer Security |
| PCI |Payment Card Industry|


- SSL certificates, TLS certificates: are incompatible with each other; they use different protocols and algorithms.
- TLS has been vulnerable to breaches such as Crime and Heartbleed in 2012 and 2014

- TLS 1.0 is effectively SSL 3.1.
> The name change from SSL to TLS was made to reflect improvements and changes in the protocol,
> as well as to avoid the commercial implications and associations with SSL.



## Evolution of SSL and TLS:
- SSL V1 – 1994 <-- SSL start
- SSL V2 – 1995
- SSL V3 – 1996
- TLS 1.0 – 1999 <-- TLS start
- TLS 1.1 – 2006
- TLS 1.2 – 2008
- SSL proven insecure - 2014 <--POODLE
- TLS 1.3 – 2015
- HTTP/2 - 2015 <-- upgrade from HTTP/1
- HTTP/3 (uses QUIC on UDP) solves HTTP/2 head-of-line blocking
> HTTP/3 developed by: Cloudflare, Google, and Mozilla.
>
> 07/2024; Only about 10% of sites support QUIC, because it is UDP and not TCP based.
>
>  Used in content distribution networks

### TLS
- TLS can work on different ports
- Uses robust encryption algorithms like keyed-HMAC (Hash-based Message Authentication Code)
- TLS can also be used by an intermediate authority, not necessarily a Certificate Authority.
### SSL
- SSL only uses MAC (Message Authentication Code)


## Extra:
- https://en.wikipedia.org/wiki/Elliptic_curve
- https://cryptobook.nakov.com/digital-signatures/rsa-signatures
- https://www.stackscale.com/blog/http2/
- https://www.cloudflare.com/learning/performance/what-is-http3/
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf
