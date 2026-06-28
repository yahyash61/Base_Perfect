const hre = require("hardhat");

async function main() {
  const HelloBase = await hre.ethers.getContractFactory("HelloBase");
  const helloBase = await HelloBase.deploy();

  await helloBase.waitForDeployment();
  console.log(`HelloBase deployed to: ${await helloBase.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});perfect Project
Safe Project
..........
Amazing Project
best............./
