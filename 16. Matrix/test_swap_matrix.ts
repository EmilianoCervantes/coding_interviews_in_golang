function solution(matrix: number[][], commands: string[]): number[][] {
  const finalMatrix: number[][] = matrix
  
  for (let i=0; i<commands.length;i+=1) {
      const commandParts = commands[i].split(" ")
      const order = commandParts[0]
      const position1 = commandParts[1]
      const position2 = commandParts[2]
      
      switch (order) {
      case "swapRows":
          const tempRow1 = finalMatrix[position1]
          finalMatrix[position1] = finalMatrix[position2]
          finalMatrix[position2] = tempRow1
          break;
      case "swapColumns":
          // Example: 1 with 2
          const tempRow00 = finalMatrix[0][position1]
          const tempRow10 = finalMatrix[1][position1]
          const tempRow20 = finalMatrix[2][position1]
          finalMatrix[0][position1] = finalMatrix[0][position2]
          finalMatrix[1][position1] = finalMatrix[1][position2]
          finalMatrix[2][position1] = finalMatrix[2][position2]
          finalMatrix[0][position2] = tempRow00
          finalMatrix[1][position2] = tempRow10
          finalMatrix[2][position2] = tempRow20
          break;
      case "reverseRow":
          const row = finalMatrix[position1]
          const tempRowAt0 = row[0]
          row[0] = row[2]
          row[2] = tempRowAt0
          break;
      case "reverseColumn":
          const tempRow0x = finalMatrix[0][position1]
          finalMatrix[0][position1] = finalMatrix[2][position1]
          finalMatrix[2][position1] = tempRow0x
          break;
      case "rotate90Clockwise":
          const esquinaSuperiorIzq = finalMatrix[0][0]
          const esquinaSuperiorDerecha = finalMatrix[0][2]
          const esquinaInferiorIzq = finalMatrix[2][0]
          const esquinaInferiorDerecha = finalMatrix[2][2]
          
          finalMatrix[0][0] = esquinaInferiorIzq
          finalMatrix[0][2] = esquinaSuperiorIzq
          finalMatrix[2][2] = esquinaSuperiorDerecha
          finalMatrix[2][0] = esquinaInferiorDerecha
          
          const midUp = finalMatrix[0][1]
          const midRight = finalMatrix[1][2]
          const midDown = finalMatrix[2][1]
          const midLeft = finalMatrix[1][0]
          
          finalMatrix[0][1] = midLeft
          finalMatrix[1][2] = midUp
          finalMatrix[2][1] = midRight
          finalMatrix[1][0] = midDown
          break;
      default:
          break;
      }
  }
  
  return finalMatrix
}
