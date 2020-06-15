# Am I Wearing a Mask?


# Deploy

```
docker build . --tag robertkarl/amiwearingamask
docker run -p5000:80 robertkarl/amiwearingamask:latest
```

- [ ] Move DNS to point to hosting provider
- [ ] In hosting provider, have the url point to kubernetes load balancer
- [ ] add a route to the ingress to point to the demo
- [ ] Create the service and deployment.
    - [ ] at this point, should be able to access the site without SSL
- [ ] Add the site and pointer to the deployment in the ingress configuration.
  - [ ] This should trigger SSL configuration
  - [ ] check challenges `kubectl get challenges.acme.cert-manager.io -n newsite-staging`
  - [ ] check certificate request: `kubectl -n velvetax-staging get certificaterequests.cert-manager.io  -o json`
